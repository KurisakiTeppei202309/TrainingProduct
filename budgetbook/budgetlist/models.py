from django.db import models

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


class Payment(models.Model):
    class Meta:
        db_table='types'
    
    name = models.CharField(verbose_name='支払方法', max_length=255)
    def __str__(self):
        return self.name


class Transactions(models.Model):
	# 記事モデル
    class Meta:
    	# テーブル名定義
    	db_table = 'transactions'

    # テーブルフィールド定義
    #created_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    amount = models.IntegerField(verbose_name='金額', default=0)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE,verbose_name='支払方法',null=True, blank=True)
    note = models.TextField(verbose_name='備考', max_length=1000,null=False, blank=True)