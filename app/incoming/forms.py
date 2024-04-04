from django import forms

from .models import Action, Incoming


class ActionForm(forms.ModelForm):

    class Meta:
        model = Action
        fields = ("name",)


class IncomingForm(forms.ModelForm):

    class Meta:
        model = Incoming
        fields = (
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