from django import forms
from budgetlist.models import Transactions,Category,Payment

class TransactionsCreateForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('amount','category','payment','note')#'date'
        # widgets = {
        # }
    #def clean_date(self):


    def clean_amount(self):
        value = self.cleaned_data['amount']
        if value < 1:
            raise forms.ValidationError(
                '%(min_length)s円以上で入力してください', params={'min_length': 1})
        return value

    def clean_category(self):
        value = self.cleaned_data['category']
        return value
    
    def clean_payment(self):
        value = self.cleaned_data['payment']
        return value

    def clean_note(self):
        value = self.cleaned_data['note']
        return value


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','category_type')


    def clean_name (self):
        value = self.cleaned_data['name']
        if Category.objects.filter(name=value).exists():
            raise forms.ValidationError('入力したカテゴリはすでに登録済みです。')
        return value

    def clean_category_type(self):
        value = self.cleaned_data['category_type']
        return value

class PaymentCreateForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('name',)

    def clean_name (self):
        value = self.cleaned_data['name']
        if Payment.objects.filter(name=value).exists():
            raise forms.ValidationError('この値はすでに存在します。')
        return value
