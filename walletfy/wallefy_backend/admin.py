from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)

admin.site.register(UserPreferenceDetails)
admin.site.register(Location)

admin.site.register(UserLocationWisePreferences)

admin.site.register(UserExpense)
