from django.urls import path
from . import views


app_name = 'budgetlist' 

urlpatterns = [
    path('',views.TransactionsCreate.as_view(), name='transactions_create') ,
    path('Category/',views.CategoryCreate.as_view(), name='category_create') ,
    path('Type/',views.TypesCreate.as_view(), name='types_create') ,
    path('Transactionslist/',views.TransactionsList.as_view(), name='transactions_list') ,
    path('Transactions_Categorylist/',views.Transaction_list_by_category.as_view(), name='transactions_list_category') ,

    
]