from django.contrib import admin
from .models import *



class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)




class TourAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tour._meta.fields]

    class Meta:
        model = Tour


admin.site.register(Tour, TourAdmin)


class Post_listAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post_list._meta.fields]

    class Meta:
        model = Post_list


admin.site.register(Post_list, Post_listAdmin)






