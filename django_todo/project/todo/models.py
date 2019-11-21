from django.db import models

# Create your models here.
# カテゴリー
class Category(models.Model):
    title = models.CharField("タイトル", max_length=20)
    def __str__(self):
        return self.title

# タイトルや日付テーブルとカテゴリーを紐付ける。
# 紐付いているデータが存在すればデータは消されなくなる。
class Todo(models.Model):
    title = models.CharField('タイトル', max_length=50)
    created_at = models.DateTimeField('日付', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    def __str__(self):
        return self.titile