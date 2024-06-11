from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Member)
admin.site.register(ConferenceAgenda)
admin.site.register(PartAgenda)
admin.site.register(ConferenceSection)
