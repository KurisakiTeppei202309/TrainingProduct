from django import forms
from budgetlist.models import Transactions,Category,Types


class TransactionsCreateForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('date','amount','category','types','note')
        # widgets = {
        #     'date':forms.DateTimeInput(format='%Y-%m-%d %H:%M：%S', attrs={'type': 'datetime-local'})
        # }

    def clean_date(self):
        value = self.cleaned_data['date']
        return value

    def clean_amount(self):
        value = self.cleaned_data['amount']
        if value < 1:
            raise forms.ValidationError(
                '%(min_length)s円以上で入力してください', params={'min_length': 1})
        return value

    def clean_category(self):
        value = self.cleaned_data['category']
        return value
    
    def clean_Types(self):
        value = self.cleaned_data['types']
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

class TypesCreateForm(forms.ModelForm):
    class Meta:
        model = Types
        fields = ('name',)

    def clean_name (self):
        value = self.cleaned_data['name']
        if Types.objects.filter(name=value).exists():
            raise forms.ValidationError('この値はすでに存在します。')
        return value

