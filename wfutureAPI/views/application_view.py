from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from ..models.volunteer_volunteership import VolunteerVolunteership

from ..templatetags.user_type_tags import is_company, is_volunteer

from ..forms import ApplicationStatusForm

from ..models.volunteership import Volunteership
from django.contrib import messages
from ..models.application import Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required
@user_passes_test(is_volunteer)
def application_list(request):
    volunteer = request.user.volunteer
    applications = Application.objects.filter(volunteer=volunteer).order_by('-created_at')
    applications = Paginator(applications, 5)
    page_number = request.GET.get("page")
    page_obj = applications.get_page(page_number)
    return render(request, 'pages/my_applications.html', context={
        'page_obj': page_obj
    })

@login_required
@user_passes_test(is_company)
def applicants_list(request, id):
    if request.method == 'POST':
        form = ApplicationStatusForm(request.POST)
        if form.is_valid():
            application_id = form.cleaned_data['application_id']
            new_status = form.cleaned_data['status']
            application = Application.objects.get(id=application_id)
            application.status = new_status
            application.save()
            relation_exists = VolunteerVolunteership.objects.filter(volunteership=application.volunteership, volunteer=application.volunteer).exists()
            if application.status == 'approved':
                if not relation_exists:
                    VolunteerVolunteership.objects.create(volunteer = application.volunteer, volunteership = application.volunteership)
            elif application.status in ['rejected', 'pending']:
                if relation_exists:
                    VolunteerVolunteership.objects.filter(volunteership=application.volunteership, volunteer=application.volunteer).delete()
            messages.success(request, 'Application status updated successfully!')
            return redirect('wfutureAPI:volunteership-applicants', id=id)
        
    volunteering = get_object_or_404(Volunteership, pk=id)
    applications = Application.objects.filter(volunteership=volunteering).order_by('-created_at')
    applications = Paginator(applications, 5)
    page_number = request.GET.get("page")
    page_obj = applications.get_page(page_number)
    return render(request, 'pages/company_volunteership_applications.html', context={
        'page_obj': page_obj
    })
    