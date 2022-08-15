from django.contrib import admin

from .models import Friend, Good, Group, Message

# Register your models here.
admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Good)
admin.site.register(Group)
