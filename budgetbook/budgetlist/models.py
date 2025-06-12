from django.db import models

# Create your models here.

class Budget(models.Model):
	# 記事モデル
    class Meta:
    	# テーブル名定義
    	db_table = 'budget'

    # テーブルフィールド定義
    #created_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    price = models.IntegerField(verbose_name='金額', default=0)
    category = models.Foreignkey(Category, on_delete=models.CASCADE)
    Payment = models.Foreignkey(Payment, on_delete=models.CASCADE,null=True, blank=True)

class Category(models.Model):
	# 記事モデル
    class Meta:
    	# テーブル名定義
    	db_table = 'category'

    name = models.CharField(verbose_name='種別', max_length=255)
    category = models.CharField(verbose_name='収支', max_length=255)

class Payment(models.Model):
    class Meta:
        db_table='types'
    
    name = models.CharField(verbose_name='支払方法', max_length=255)

