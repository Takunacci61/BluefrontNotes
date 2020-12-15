from django.contrib import admin
from .models import Profile_Pic, Local_Authority, YP_General_Information,Care_House_Information, YP_Contact_Info, \
    YP_Profile_Child, YP_Pen_Pic, YP_Health_And_Wellness, YP_IPA, YP_Physical_Description,  YP_Banking_Information, YP_Relationships_Associates


admin.site.register(Profile_Pic)
admin.site.register(Local_Authority)
admin.site.register(YP_General_Information)
admin.site.register(Care_House_Information)
admin.site.register(YP_Contact_Info)
admin.site.register(YP_Pen_Pic)
admin.site.register(YP_Health_And_Wellness)
admin.site.register(YP_IPA)
admin.site.register(YP_Physical_Description)
admin.site.register(YP_Banking_Information)
admin.site.register(YP_Profile_Child)
admin.site.register(YP_Relationships_Associates)
