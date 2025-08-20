from django import forms

from .models import Exam


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["name", "date", "duration"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
