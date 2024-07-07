from django.shortcuts import get_object_or_404, redirect, render

from ..models.user_certificate import UserCertificate

from ..models.review import Review

from ..models.volunteer import Volunteer

from ..models.volunteer_volunteership import VolunteerVolunteership

from ..models.location import Location

from ..forms import ReviewForm, VolunteerStatusForm, VolunteershipForm

from ..templatetags.user_type_tags import is_company, is_volunteer

from ..models.application import Application
from ..models.city import City
from ..models.cause import Cause
from ..models.skill import Skill
from django.core.paginator import Paginator
from ..models.volunteership import Volunteership
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def volunteership_list(request):
    volunteerings = Volunteership.objects.all()
    causes = Cause.objects.all()
    skills = Skill.objects.all()
    cities = City.objects.all()
    title_contains = request.GET.get('title_contains')
    cause = request.GET.get('cause')
    skill=request.GET.get('skill')
    city=request.GET.get('city')
    if(title_contains): 
        volunteerings = volunteerings.filter(title__icontains=title_contains)
    if(cause):
        volunteerings = volunteerings.filter(causevolunteerships__cause__name = cause)
    if(skill):
        volunteerings = volunteerings.filter(skillvolunteerships__skill__name = skill)
    if(city):
        volunteerings = volunteerings.filter(location__city__name = city)

    volunteerings = Paginator(volunteerings, 5)
    page_number = request.GET.get("page")
    page_obj = volunteerings.get_page(page_number)
    return render(request, 'pages/volunteerships.html', context={
        'page_obj':  page_obj,
        'causes': causes,
        'skills': skills,
        'cities': cities
    })

def volunteer_volunteerships_list(request) :
    volunteerings = VolunteerVolunteership.objects.filter(volunteer=request.user.volunteer).select_related('volunteership').order_by('created_at')
    print(volunteerings)
    volunteerings = Paginator(volunteerings, 5)
    page_number = request.GET.get("page")
    page_obj = volunteerings.get_page(page_number)
    isempty = True
    if page_obj.object_list.count() > 0:
        isempty = False

    return render(request, 'pages/volunteerships_list.html', context={
        'page_obj':  page_obj,
        'is_empty': isempty
    })

def volunteership_detail(request, id):
    volunteering = get_object_or_404(Volunteership,id=id)
    skills = volunteering.skills.all()
    causes = volunteering.causes.all()
    if(hasattr(request.user, 'volunteer')):
        volunteer = request.user.volunteer
        if Application.objects.filter(volunteership=volunteering, volunteer=volunteer).exists():
            return render(request, 'pages/volunteership_page.html', context={
            'volunteering': volunteering,
            'skills': skills,
            'causes': causes,
            'has_applied': True
        })
    return render(request, 'pages/volunteership_page.html', context={
        'volunteering': volunteering,
        'skills': skills,
        'causes': causes
    })

from django.contrib import messages

def my_reviews(request): 
    reviews = Review.objects.filter(volunteer=request.user.volunteer)
    return render(request,'pages/my_reviews.html', {'reviews': reviews})


@user_passes_test(is_company)
def give_review(request, volunteer_id, volunteership_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    volunteership = get_object_or_404(Volunteership, id=volunteership_id)
    company = volunteership.company  

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.volunteer = volunteer
            review.volunteership = volunteership
            review.company = company
            review.save()
            return redirect('wfutureAPI:volunteers_for_volunteership', id=volunteership_id)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'volunteer': volunteer,
        'volunteership': volunteership,
        'company': company,
    }
    return render(request, 'pages/review_page.html', context)



def volunteers_for_volunteership(request, id):
    volunteership = get_object_or_404(Volunteership, id=id)
    volunteer_volunteerships = VolunteerVolunteership.objects.filter(volunteership=volunteership).order_by('-created_at')

    if request.method == 'POST':
        form = VolunteerStatusForm(request.POST)
        if form.is_valid():
            volunteer_volunteership_id = form.cleaned_data['volunteer_volunteership_id']
            new_status = form.cleaned_data['status']
            volunteer_volunteership = get_object_or_404(VolunteerVolunteership, id=volunteer_volunteership_id)
            volunteer_volunteership.status = new_status
            print(volunteer_volunteership.recieved_points)
            if new_status == 'finished' and not volunteer_volunteership.recieved_points:
                volunteer = volunteer_volunteership.volunteer
                volunteership_points = volunteer_volunteership.volunteership.points
                volunteer.points += volunteership_points
                volunteer.save()
                volunteer_volunteership.recieved_points = True
                userCertificate = UserCertificate.objects.create(volunteer=volunteer, volunteership=volunteership, date_of_completion=volunteership.end_date)
                print(userCertificate)
            volunteer_volunteership.save()
            messages.success(request, 'Volunteer status updated successfully!')
            return redirect('wfutureAPI:volunteers_for_volunteership', id=id)
    
    paginator = Paginator(volunteer_volunteerships, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'volunteership': volunteership,
        'page_obj': page_obj,
        'form': VolunteerStatusForm(),
    }
    return render(request, 'pages/volunteers_list.html', context)


@login_required
@user_passes_test(is_volunteer)
def apply_for_volunteering(request, id):
    volunteering = get_object_or_404(Volunteership, pk=id)
    volunteer = request.user.volunteer

    if Application.objects.filter(volunteership=volunteering, volunteer=volunteer).exists():
        return render('wfutureAPI:volunteership-detail', id=id, context={'has_applied': True})

    Application.objects.create(volunteership=volunteering, volunteer=volunteer)

    return redirect('wfutureAPI:volunteership-detail', id=id)

@login_required
@user_passes_test(is_company)
def my_volunteerships(request):
    company = request.user.company
    company_volunteerships = company.volunteership_set.all().order_by('-created_at')
    paginator = Paginator(company_volunteerships, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/my_volunteerships.html', {'page_obj': page_obj})

@user_passes_test(is_company)
def create_volunteership(request):
    if request.method == 'POST':
        form = VolunteershipForm(request.POST, request.FILES)
        if form.is_valid():
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            
            location = Location.objects.create(
                country=country,
                city=city,
                address=address
            )
            
            volunteership = form.save(commit=False)
            volunteership.location = location
            volunteership.company = request.user.company 
            volunteership.save()
            form.save_m2m()
            return redirect('wfutureAPI:my-volunteerships') 
    else:
        initial_data = {'company': request.user.company}  
        form = VolunteershipForm(initial=initial_data)
    
    return render(request, 'pages/new_volunteership.html', {'form': form})
