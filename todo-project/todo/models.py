from django.db import models

# Create your models here.

CHOICE = (("danger", "high"),("warning", "normal"),("primary", "low"))#第一引数は、機械が見る。第二因数は、画面に表示される

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE #上に定義されている変数CHOISEを代入
        )
    duedate = models.DateField()#データを日付として受け取れる
# オブジェクトが実行されたときに実行される関数
    def __str__(self):
        return self.title