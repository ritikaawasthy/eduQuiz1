from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .validators import validate_email
from django.forms import ModelForm
from .models import Question, Answer


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class QuestionForm(ModelForm):
    class Meta:
        model= Question
        fields= "__all__"
        #fields= ['name', 'picture', 'ability', 'ans', 'option1','option2','option3','option4']

class AnswerForm(ModelForm):
    class Meta:
        model= Answer
        fields= "__all__"
