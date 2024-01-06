from django import forms
from .models import Apply, Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = [
            "name",
            "email",
            "website",
            "cv",
            "cover_letter"
        ]


class AddJob(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "job_type",
            "description",
            "published_at",
            "vacancy",
            "salary",
            "experience",
            "category",
            "image"
        ]