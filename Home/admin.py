from django.contrib import admin
from Home.models import *
# Register your models here.
admin.site.register([Blog,Comment,Tag,Category])