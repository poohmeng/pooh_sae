__author__ = 'mengmeng'
from django import forms as forms

class ContactForm(forms.Form):
    # subject = forms.ChoiceField(choices=TOPIC_CHOICES)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea())
    from_email = forms.EmailField(required=False,label='Your e-mail address')
    # def clean_message(self):
    #     message = self.cleaned_data.get('message', '')
    #     num_words = len(message.split())
    #     if num_words < 4:
    #         raise forms.ValidationError("Not enough words!")
    #     return message