from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'questions'
