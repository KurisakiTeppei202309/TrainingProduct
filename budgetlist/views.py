from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, TemplateView,ListView
from budgetlist.models import Transactions,Category,Types
from budgetlist.forms import TransactionsCreateForm,CategoryCreateForm,TypesCreateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render (request,'base.html')

class TransactionsCreate (View):
    def get(self, request, *args, **kwargs):
        form =TransactionsCreateForm()
        context = {
            'form' : form,
        }
        return render(request, 'budgetlist/transactions_form.html', context)

    def post(self, request, *args, **kwargs):
        form =TransactionsCreateForm(request.POST)
        if not form.is_valid():
            context = {
                'form' : form,
            }
            return render(request, 'budgetlist/transactions_form.html', context)

        transactions = Transactions()
        transactions.date = form.cleaned_data.get('date')
        transactions.amount = form.cleaned_data.get('amount')
        transactions.category = form.cleaned_data.get('category')
        transactions.types = form.cleaned_data.get('types')
        transactions.note = form.cleaned_data.get('note')
        transactions.save()
        queryset = Transactions.objects.all().order_by('id')
        context = {
                'transactions_list' : queryset,
            }
        return render(request,'budgetlist/transactions_list.html',context)

class CategoryCreate(View):
    def get(self, request, *args, **kwargs):
        form = CategoryCreateForm()
        context = {
            'form' : form,
        }
        return render(request, 'budgetlist/category_form.html', context)
    def post(self, request, *args, **kwargs):
        form = CategoryCreateForm(request.POST)
        if not form.is_valid():
            context = {
                'form' : form,
            }
            return render(request, 'budgetlist/category_form.html', context)
        category = Category()
        category.name = form.cleaned_data.get('name')
        category.category_type = form.cleaned_data.get('category_type')
        category.save()
        queryset = Category.objects.all().order_by('id')
        context = {
            'category_list' : queryset,
        }
        return render(request, 'base.html', context)

class TypesCreate(View):
    def get(self, request, *args, **kwargs):
        form =TypesCreateForm()
        context = {
            'form' : form,
        }
        return render(request, 'budgetlist/types_form.html', context)
    def post(self, request, *args, **kwargs):
        form = TypesCreateForm(request.POST)
        if not form.is_valid():
            context = {
                'form' : form,
            }
            return render(request, 'budgetlist/types_form.html', context)
        types = Types()
        types.name = form.cleaned_data.get('name')
        types.save()
        queryset = Types.objects.all().order_by('id')
        context = {
            'types_list' : queryset,
        }
        return render(request, 'base.html', context)

class TransactionsList(ListView):
    # template_name = 'budgetlist/transactions_list.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) #親クラスの関数を取得
    #     context['transactionslist'] = Transactionst.objects.all() #キーとバリューの追加
    model = Transactions 


class Transaction_list_by_category(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'budgetlist/transactions_categorylist.html')

    def post(self, request, *args, **kwargs):
        # try:
        category_id = int(self.request.POST.get('category_id'))
        category = Transactions.objects.filter(category=category_id)
        # except Department.DoesNotExist:
        #     raise Http500("Department does not exist")
        context = {
            'transactions_list' : category,
        }
        return render(request, 'budgetlist/transactions_categorylist.html', context)


    
