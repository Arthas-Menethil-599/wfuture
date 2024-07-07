from django.urls import path

from .views.cetificate_view import generate_certificate, my_certificates

from .views.user_profile_view import user_profile

from .views.application_view import applicants_list, application_list

from .views import storeitem_list

from .views.home_view import home
from .views.storeitem_view import storeitem_list
from .views.storeitem_view import storeitem_detail
from .views.companies_view import company_list
from .views.volunteerships_view import create_volunteership, give_review, my_reviews, my_volunteerships, volunteer_volunteerships_list, volunteers_for_volunteership, volunteership_list, apply_for_volunteering, volunteership_detail
from .views.authorization_view import company_signup_view, login_view, signup_selection_view, volunteer_signup_view, logout_view

app_name = 'wfutureAPI'

urlpatterns = [
    path('', home, name="home"),
    path('volunteerings/', volunteership_list, name="volunteerships"),
    path('volunteerings/<int:id>/', volunteership_detail, name="volunteership-detail"),
    path('volunteerings/new/', create_volunteership, name='create_volunteership'),
    path('companies/', company_list, name="companies"),
    path('coinstore/', storeitem_list, name='coinstore'),
    path('login/', login_view, name="login"),
    path('signup', signup_selection_view, name="signup_selection"),
    path('signup/volunteer/', volunteer_signup_view, name='signup_volunteer'),
    path('signup/company/', company_signup_view, name='signup_company'),
    path('logout/', logout_view, name='logout'),
    path('applications/', application_list, name="my-applications"),
    path('applicants/<int:id>/', applicants_list, name="volunteership-applicants"),
    path('my_volunteerships/', my_volunteerships, name='my-volunteerships'),
    path('volunteerings/<int:id>/apply/', apply_for_volunteering, name='apply_for_volunteering'),
    path('volunteerings/<int:id>/volunteers/', volunteers_for_volunteership, name='volunteers_for_volunteership'),
    path('give-review/<int:volunteer_id>/<int:volunteership_id>/', give_review, name='give_review'),
    path('volunteers_volunteerings/', volunteer_volunteerships_list, name='volunteer-volunteerships-list'),
    path('coinstore/<int:id>/', storeitem_detail,
         name='storeitem_detail'),
    path('profile/<int:id>/', user_profile, name='user-profile'),
    path('certificate/<int:id>/', generate_certificate, name='generate-certificate'),
    path('my_certificates', my_certificates, name="my-certificates"),
    path('my_reviews', my_reviews, name="my-reviews")
]