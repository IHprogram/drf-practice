from django.db import models

class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    content = models.TextField('本文')
    created_at = models.DateTimeField('作成日', auto_now_add=True)

    # __str__関数は文字列表現を定義するための特殊メソッド。ここではtitleを返す
    def __str__(self):
        print(self)
        return self.title