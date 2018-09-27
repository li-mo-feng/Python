from django.db import models

# Create your models here.
class grade(models.Model):
    grade_id=models.IntegerField(primary_key=True)
    # 列名。整形
    grade_name=models.CharField(max_length=20)
    # 列名，字符型
    grade_size=models.IntegerField()
    # 列名，班级容量，人数
    grade_money=models.FloatField()
    # 列名，班费，浮点数
    grade_img=models.CharField(max_length=20)


class student(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=20,unique=True)
    stu_grade_id=models.ForeignKey("grade")


