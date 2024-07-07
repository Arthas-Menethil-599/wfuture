from django.shortcuts import render, get_object_or_404

from ..models.skill_volunteer import SkillVolunteer
from django.contrib.auth.models import User
from ..models.skill import Skill

from ..templatetags.user_type_tags import is_volunteer

def user_profile(request, id):
    user = get_object_or_404(User, id=id)
    volunteer = getattr(user, 'volunteer', None)
    company = getattr(user, 'company', None)
    if volunteer is not None:
        skills = volunteer.skills.all() if hasattr(volunteer, 'skills') else []
        context = {
            'volunteer': volunteer,
            'skills': skills,
            'id': id
        }
        return render(request, 'pages/user_profile.html', context)
    elif company is not None:
        context = {
            'company': company,
            'id': id
        }
        return render(request, 'pages/company_profile.html', context)
    else:
        return render(request, 'pages/no_profile.html', {'id': id})
    