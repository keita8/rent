from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Mot de passe',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmer votre mot de passe',
        'class'      : 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['placeholder'] = 'Votre pseudo'
        self.fields['email'].widget.attrs['placeholder'] = 'Votre adresse email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password :
            raise forms.ValidationError("Les mots de passe doivent être identiques")




class UserForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Votre adresse email'
        self.fields['password'].widget.attrs['placeholder'] = 'Votre mot de passe'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
