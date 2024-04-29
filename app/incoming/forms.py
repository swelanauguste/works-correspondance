from django import forms

from .models import Incoming


class IncomingForm(forms.ModelForm):

    class Meta:
        model = Incoming
        fields = (
            "file",
            "subject",
            "received",
            "dated",
            "rfrom",
            "to",
            "cc",
            "action",
            "forward",
            "notes",
        )
        widgets = {
            "received": forms.DateInput(attrs={"type": "date"}),
            "dated": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 2}),
        }
