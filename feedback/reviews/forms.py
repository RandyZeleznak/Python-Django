from django import forms

from .models import Review


# class ReviewForm(forms.Form):
#    user_name = forms.CharField(
#        label="Your Name", max_length=50,
#        error_messages={"required": "Name required"})
#    review_text = forms.CharField(
#        label="Your feedback", widget=forms.Textarea, max_length=200)
#    rating = forms.IntegerField(label="rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        #fields = ['user_name','review_text','rating']
        #exclude = ['owner_comment']
        labels = {
            "user_name": "Your Name",
            "review_text": " Your Feelings",
            "rating": "Your Rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name"
            }
        }