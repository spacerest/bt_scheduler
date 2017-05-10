from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
	    raise forms.ValidationError("Minimum number of words is 4, you have %s:)."% num_words)
	elif num_words > 1000:
	    raise forms.ValidationError("Maximum number of words is 1000, you have %s:)." % num_words)
	return message


