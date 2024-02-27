from django.contrib import admin
from . models import *
# Register your models here.
readonly_fields = ('id',)
admin.site.register(RegisterU)
