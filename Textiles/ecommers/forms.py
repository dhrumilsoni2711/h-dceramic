from django import forms

#######################################################################
##################### Admin Login #####################################


class AdminLoginForm(forms.Form):
    a_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-box'})
    )
    a_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-box'})
    )

    
    
