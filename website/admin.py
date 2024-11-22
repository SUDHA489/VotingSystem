from django.contrib import admin
from .models import Voter,Ballot
# Register your models here.
admin.site.register(Voter)
admin.site.register(Ballot)