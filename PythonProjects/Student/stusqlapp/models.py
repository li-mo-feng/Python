from django.db import models

# Create your models here.
class stu_infor(models.Model):
    objects = models.Manager()
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=20)
    stu_password=models.IntegerField()
    stu_grade_id=models.IntegerField()


class grade(models.Model):
    grade_id=models.IntegerField(primary_key=True)
    grade_money=models.IntegerField()
    grade_name=models.CharField(max_length=20)