from django.urls import path
from . import views


app_name = 'budgetlist' 

urlpatterns = [
    path('',views.index, name='top') ,
    path('Transactions/',views.TransactionsCreate.as_view(), name='transactions_create') ,
    path('Category/',views.CategoryCreate.as_view(), name='category_create') ,
    path('Payment/',views.PaymentCreate.as_view(), name='payment_create') ,
  
]