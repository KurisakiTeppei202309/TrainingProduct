from django import forms

from django import forms
from budgetlist.models import Budget

class CreateInputForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('date', 'price','category','payment')
        widgets = {
            
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }
    #def clean_date(self):


    def clean_price(self):
        value = self.cleaned_data['price']
        if len(value) < 1:
            raise forms.ValidationError(
                '%(min_length)s円以上で入力してください', params={'min_length': 1})
        return value

    def clean_category(self):
        value = self.cleaned_data['category']
        return value

    def clean_payment(self):
        value = self.cleaned_data['payment']
        return value


