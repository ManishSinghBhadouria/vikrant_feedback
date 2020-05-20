from django.contrib import admin
from .models import registration,facprofile,stdprofile,subject,subjectallotment,feedbackreg,startfeedback,notes
# Register your models here.

admin.site.register(registration)
admin.site.register(facprofile)
admin.site.register(stdprofile)
admin.site.register(subject)
admin.site.register(subjectallotment)
admin.site.register(feedbackreg)
admin.site.register(startfeedback)
admin.site.register(notes)