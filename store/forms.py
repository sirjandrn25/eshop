from django import forms
from .models.customers import Customer

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','email','phone','password')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name',}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'example@gmail.com'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Number'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}),
        }
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = Customer.objects.get(email = email)
        except:
            return email
        raise forms.ValidationError("This email is already exists")
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password)<=6:
            raise forms.ValidationError("Password length is greater than 6 needed")
        elif password.isdigit():
            raise forms.ValidationError("Only Digit is not valid")
        else:
            return password
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if len(str(phone))<10 or len(str(phone))>10:
            raise forms.ValidationError("Enter the number 10 digits")
        else:
            return phone