from django.contrib import admin

from .models import Doctor, User, Preference, Specialty, Insurance

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Insurance)
admin.site.register(Specialty)
admin.site.register(User)
admin.site.register(Preference)


