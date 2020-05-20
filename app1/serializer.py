from rest_framework import serializers
from .models import registration,facprofile,stdprofile,subject,subjectallotment,feedbackreg,startfeedback,notes

class registrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = registration
        fields = "__all__"
    
class facprofileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = facprofile
        fields = "__all__"

class stdprofileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = stdprofile
        fields = "__all__"
    
class subjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = subject
        fields = "__all__"


class subjectallotmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = subjectallotment
        fields = "__all__"
    
class feedbackregSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = feedbackreg
        fields = "__all__"

class startfeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = startfeedback
        fields = "__all__"
    
class notesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = notes
        fields = "__all__"
