from django import forms

from .models import Rating

REVIEW_POINT_CHOICES = (
    (1, '#시간아까움'),
    (2, '#시간 때우기용'),
    (3, '#한번쯤 볼만함'),
    (4, '#만족스러움'),
    (5, '#나의 인생작'),
)

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['comment_text', 'rating']

        widgets = {
            'rating' : forms.Select(choices=REVIEW_POINT_CHOICES)
        }
        
