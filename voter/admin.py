from django.contrib import admin
from  .models import Candidates, Voter, Admin
# Register your models here.
admin.site.register(Admin)
admin.site.register(Voter)
admin.site.register(Candidates)