from django import template
from ..models.volunteer import Volunteer
from ..models.company import Company

register = template.Library()

@register.filter(name='is_volunteer')
def is_volunteer(user):
    return hasattr(user, 'volunteer') and user.volunteer is not None

@register.filter(name='is_company')
def is_company(user):
    return hasattr(user, 'company')
