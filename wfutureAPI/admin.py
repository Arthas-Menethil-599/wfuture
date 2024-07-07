from django.contrib import admin

from .models.user_certificate import UserCertificate
from .models.application import Application
from .models.cause_volunteerships import CauseVolunteerships
from .models.cause import Cause
from .models.city import City
from .models.company import Company
from .models.country import Country
from .models.location import Location
from .models.review import Review
from .models.skill_volunteer import SkillVolunteer
from .models.skill_volunteerships import SkillVolunteerships
from .models.skill import Skill
from .models.storeitem import StoreItem
from .models.volunteer_volunteership import VolunteerVolunteership
from .models.volunteer import Volunteer
from .models.volunteership_like import VolunteershipLike
from .models.volunteership import Volunteership

admin.site.register(Application)
admin.site.register(CauseVolunteerships)
admin.site.register(Cause)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Review)
admin.site.register(SkillVolunteer)
admin.site.register(SkillVolunteerships)
admin.site.register(Skill)
admin.site.register(StoreItem)
admin.site.register(VolunteerVolunteership)
admin.site.register(Volunteer)
admin.site.register(VolunteershipLike)
admin.site.register(Volunteership)
admin.site.register(UserCertificate)