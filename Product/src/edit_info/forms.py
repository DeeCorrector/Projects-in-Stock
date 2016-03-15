from django import forms

from web.models import Project

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "topic",
            "degree"
        ]
