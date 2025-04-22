from django import forms
from books.models import Reviews



class ReviewForm(forms.ModelForm):
    review_txt = forms.CharField(widget=forms.Textarea(attrs={'class' : "border rounded p-2 w-full m-10",
          'name' : "review",
          'placeholder' : "Enter Your Review Here",
          'rows' : 4}))
                                 
    class Meta:
        model = Reviews
        fields = ['review_txt']


