from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, TemplateView
from budgetlist.models import Transactions,Category,Payment
from budgetlist.forms import TransactionsCreateForm,CategoryCreateForm,PaymentCreateForm


# Create your views here.
def index(request):
    return render (request,'base.html')

class TransactionsCreate (View):
    # form_class = TransactionsCreateForm

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(TransactionsCreate, self).form_valid(form)
    # fields = ['price','category','payment']
    # success_url= reverse_lazy('transactionslist:transactions_create')#登録成功した際の遷移先を指定
    
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
        transactions.amount = form.cleaned_data.get('amount')
        form_category_name=form.cleaned_data.get('category')
        category = Category.objects.get(name=form_category_name)
        transactions.category = form_category_name

        transactions.payment = form.cleaned_data.get('payment')
        transactions.note = form.cleaned_data.get('note')
        transactions.save()
        queryset = Transactions.objects.all().order_by('id')
            # context = {
            #     'transactions_list' : queryset,
            #}
        # except category.DoesNotExist:
        #     raise Http500("category does not exist")
        #     # return redirect(reverse('bizcomu:index'))
        return render(request,'base.html')#context budgetlist/transactions_list.html

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

class PaymentCreate(View):
    def get(self, request, *args, **kwargs):
        form =PaymentCreateForm()
        context = {
            'form' : form,
        }
        return render(request, 'budgetlist/payment_form.html', context)
    def post(self, request, *args, **kwargs):
        form = PaymentCreateForm(request.POST)
        if not form.is_valid():
            context = {
                'form' : form,
            }
            return render(request, 'budgetlist/payment_form.html.html', context)
        payment = Payment()
        payment.name = form.cleaned_data.get('name')
        payment.transactions_type = form.cleaned_data.get('transactions_type')
        payment.save()
        queryset = Payment.objects.all().order_by('id')
        context = {
            'payment_list' : queryset,
        }
        return render(request, 'base.html', context)
