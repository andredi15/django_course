from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#      user_name = forms.CharField(label="Your Name", max_length=10, error_messages={"required": "Name must not be empty", "max_length":"Enter a shorter name!"})
#      review_text = forms.CharField(label="Your Feedback", max_length=100, widget=forms.Textarea)
#      rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        labels = {
            'user_name':'Your Name',
            'review_text':'Your Feedback',
            'rating':'Your Rating'
        }
        error_messages={
            'user_name': {
                'required':'Your name must not be empty!'
            }
        }