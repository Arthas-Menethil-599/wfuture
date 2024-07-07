from django.shortcuts import render
from django.core.paginator import Paginator
from ..models.company import Company

def company_list(request):
    companies = Company.objects.all()
    companies = Paginator(companies, 5)
    page_number = request.GET.get("page")
    page_obj = companies.get_page(page_number)
    return render(request, 'pages/companies.html', context={
        'page_obj': page_obj
    })