from django.contrib import admin
from .models import Profile, Local_Authority, YP_General_Information,Care_House_Infomation, YP_Contact_Info


admin.site.register(Profile)
admin.site.register(Local_Authority)
admin.site.register(YP_General_Information)
admin.site.register(Care_House_Infomation)
admin.site.register(YP_Contact_Info)
