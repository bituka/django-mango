from django import forms

from conference.models import Conference


class ConferenceForm(forms.ModelForm):

    class Meta:
        model = Conference
