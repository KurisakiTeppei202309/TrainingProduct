from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, TemplateView,ListView
from budgetlist.models import Transactions,Category,Types,Expense
from budgetlist.forms import TransactionsCreateForm,CategoryCreateForm,TypesCreateForm,CategorySearchForm,ExpenseCreateForm,ExpenseSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TransactionsCreate (LoginRequiredMixin,View):
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
        transactions.expense = form.cleaned_data.get('expense')
        transactions.note = form.cleaned_data.get('note')
        transactions.user = request.user
        transactions.save()
        queryset = Transactions.objects.filter(user=self.request.user).order_by('date')
        context = {
                'transactions_list' : queryset,
            }
        return render(request,'budgetlist/transactions_list.html',context)

class CategoryCreate(LoginRequiredMixin,View):
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
        transactions_form=TransactionsCreateForm()
        context = {
            'category_list' : queryset,
            'form' : transactions_form,
        }
        return render(request, 'budgetlist/transactions_form.html', context)

class TypesCreate(LoginRequiredMixin,View):
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
        transactions_form=TransactionsCreateForm()

        context = {
            'types_list' : queryset,
            'form' : transactions_form,

        }
        return render(request, 'budgetlist/transactions_form.html', context)


class TransactionsList(LoginRequiredMixin,ListView):
    model = Transactions 
    template_name = "transactions_list.html"
    context_object_name = "transactions_list"

    

    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user).order_by("date")



class Transaction_list_by_category(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = CategorySearchForm()

        context = {
            'form' : form,
        }
        return render(request, 'budgetlist/transactions_categorylist.html', context)
    def post(self, request, *args, **kwargs):
        form = CategorySearchForm(request.POST)
        if not form.is_valid():
            context = {
                'form' : form,
            }
            return render(request, 'budgetlist/transactions_categorylist.html', context)
        category_name = form.cleaned_data.get('name')
        category = Category.objects.filter(name=category_name).first()
        transactions_category= Transactions.objects.filter(category=category.id,user=self.request.user).order_by("date")
        context = {
            'transactions_list' : transactions_category,
            'form': form, 
        }

        return render(request, 'budgetlist/transactions_categorylist.html', context)

class ExpenseCreate(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form =ExpenseCreateForm()
        context = {
            'form' : form,
        }
        return render(request, 'budgetlist/expense_form.html', context)
    def post(self, request, *args, **kwargs):
        form = ExpenseCreateForm(request.POST)
        if not form.is_valid():
            context = {
                'form' : form,
            }
            return render(request, 'budgetlist/expense_form.html', context)
        expense = Expense()
        expense.name = form.cleaned_data.get('name')
        expense.save()
        queryset = Expense.objects.all().order_by('id')
        transactions_form=TransactionsCreateForm()
        context = {
            'expense_list' : queryset,
            'form' : transactions_form,

        }
        return render(request, 'budgetlist/transactions_form.html', context)
    
class Transaction_list_by_expense(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = ExpenseSearchForm()

        context = {
            'form' : form,
        }
        return render(request, 'budgetlist/transactions_expenselist.html', context)
    def post(self, request, *args, **kwargs):
        form = ExpenseSearchForm(request.POST)
        if not form.is_valid():
            context = {
                'form' : form,
            }
            return render(request, 'budgetlist/transactions_expenselist.html', context)
        expense_name = form.cleaned_data.get('name')
        expense = Expense.objects.filter(name=expense_name).first()
        transactions_expense= Transactions.objects.filter(expense=expense.id,user=self.request.user).order_by("date")
        context = {
            'transactions_list' : transactions_expense,
            'form': form, 
        }

        return render(request, 'budgetlist/transactions_expenselist.html', context)
