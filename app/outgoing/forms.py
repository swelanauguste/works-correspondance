from django import forms

from .models import Outgoing


class OutgoingForm(forms.ModelForm):

    class Meta:
        model = Outgoing
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "date_typed": forms.DateInput(attrs={"type": "date"}),
            "out_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 2}),
        }
