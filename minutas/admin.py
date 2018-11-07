from django.contrib import admin
from .models import Minute, Meeting, Member, RefuseMinute

# Register your models here.

admin.site.register(Minute)
admin.site.register(Meeting)
admin.site.register(Member)
admin.site.register(RefuseMinute)