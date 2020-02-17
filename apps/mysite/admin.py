from django.contrib import admin
from apps.mysite.models import Album, Band, Track, InstagramPost
from apps.users.models import User 

admin.site.register(Album)
admin.site.register(Band)
admin.site.register(Track)
admin.site.register(InstagramPost)
admin.site.register(User)