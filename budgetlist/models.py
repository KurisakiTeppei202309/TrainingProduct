from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

TYPE = [
    ('1', '収入'),
    ('2', '支出'),
]

class Category(models.Model):
	# 記事モデル
    class Meta:
    	# テーブル名定義
    	db_table = 'category'
    name = models.CharField(verbose_name='カテゴリ名', max_length=255)
    category_type=models.CharField(verbose_name='種別', max_length=2, choices=TYPE,null=True)
    #オブジェクトを文字列に変換させる
    def __str__(self):
        return self.name

class Expense(models.Model):
    class Meta:
        db_table = 'expense'
    name = models.CharField(verbose_name='支払場所', max_length=255)
    def __str__(self):
        return self.name



class Types(models.Model):
    class Meta:
        db_table='types'
    
    name = models.CharField(verbose_name='受取・支払方法', max_length=255)
    def __str__(self):
        return self.name


class Transactions(models.Model):
	# 記事モデル
    class Meta:
    	# テーブル名定義
    	db_table = 'transactions'

    # テーブルフィールド定義
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='取引日時',default=timezone.now)
    amount = models.IntegerField(verbose_name='金額', default=0)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.CASCADE)
    expense =  models.ForeignKey(Expense, verbose_name='支払場所', on_delete=models.CASCADE,null=True, blank=True)
    types = models.ForeignKey(Types, on_delete=models.CASCADE,verbose_name='受取/支払方法',null=True, blank=True)
    note = models.TextField(verbose_name='備考', max_length=1000,null=False, blank=True)    