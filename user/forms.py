from django import forms
from allauth.account.forms import SignupForm
from .models import Account


class RegistrationForm(SignupForm):
    name = forms.CharField(max_length=60, label="Name", widget=forms.TextInput(attrs={'placeholder':'Name'}))

    class Meta:
        model = Account
        fields = ("email", "username", "name", "password1", "password2")


    def save(self, request):
        user = super(RegistrationForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.save()

        return user


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username', 'name', 'picture')
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'readURL(this)', 'id':'id_image_file', 'hidden':'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-3', 'id':'floatingInput', 'placeholder':"name@example.com"}),
            'username': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingUsername', 'placeholder':"username"}),
            'name': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingName', 'placeholder':"Name"}),
        }

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('username "%s" is already in use.' % account.username)