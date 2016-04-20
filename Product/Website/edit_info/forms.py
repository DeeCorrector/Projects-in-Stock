from django import forms

from web.models import Project
from web.models import Counselor

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "topic",
            "degree"
        ]

class EditCounselorInfoForm(forms.ModelForm):
    class Meta:
        model = Counselor
        fields = [
            "name",
            "email",
            "study_area",
            "office",
            "status"
        ]
