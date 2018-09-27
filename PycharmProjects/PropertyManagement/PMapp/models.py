from django.db import models

# Create your models here.
class user(models.Model):
    user_id=models.CharField(primary_key=True,max_length=18)
    # 使用者ID
    user_password=models.CharField(max_length=20,null=False)
    # 使用者密码
    user_name=models.CharField(null=False,max_length=20)
    # 使用者姓名
    user_sex=models.CharField(null=False,max_length=10)
    # 使用者性别
    user_city=models.CharField(null=False,max_length=254)
    # 使用者籍贯
    user_phonenum=models.CharField(null=False,max_length=11,unique=True)
    # 使用者联系方式
    user_roomid= models.ForeignKey("room",null=True)
    # 外键关联房间
    user_cardnum=models.CharField(max_length=18,unique=True)
    # 使用者身份证号码
    user_type=models.CharField(max_length=20)
    # 使用者身份
# -----------------------------使用人员表--------------------------



# ----------------------------楼盘表--------------------------
class building(models.Model):
    building_name=models.IntegerField(primary_key=True)
    # 楼栋号
    building_sdate=models.DateField(null=False)
    # 楼栋开工时间
    building_edate=models.DateField(null=False)
    # 楼栋完工时间
    building_floor=models.IntegerField()
    # 楼层数据
    building_bcp=models.CharField(max_length=254)
    # 楼栋施工方
    building_svcp=models.CharField(max_length=254)
    # 监理公司


# -----------------------房间信息-------------------

class room(models.Model):
    room_id=models.IntegerField(primary_key=True)
    # 房间号
    room_buildingid=models.IntegerField()
    # 所属楼栋号
    room_ownerid=models.ForeignKey("user",null=True)
    # 外键关联使用者id
    room_ownername=models.CharField(max_length=20,null=True)
#     所属业主姓名
    room_indatae=models.DateField(null=True)
#     业主入住日期
    room_s=models.IntegerField(null=False)
#     房屋面积
    room_sort=models.CharField(null=False,max_length=1)
#     房屋型号（A/B）
    room_type=models.CharField(null=False,max_length=10)
#     房屋性质
    room_property=models.CharField(null=False,max_length=10)

# ------------------------------------------------------房间信息-----------


# -------------------------物资信息---------------
class material(models.Model):
    material_id=models.IntegerField(primary_key=True)
#     物资id
    material_nmae=models.CharField(null=False,max_length=20,unique=True)
#     物资名称
    material_count=models.IntegerField(null=False)
#     物资数量
    material_price=models.IntegerField(null=False)
#     物资报价
    material_indate=models.DateField()
#     物资入库日期
    material_state=models.CharField(max_length=20)
#     物资状态
    material_type=models.CharField(max_length=20,unique=False)
#     物资类型


# ------------------------------------物资信息---------------------------
class charge(models.Model):
    charge_id=models.IntegerField(primary_key=True)
#     收费项目id
    charge_name=models.CharField(null=False,unique=True,max_length=254)
#     收费项目名称
    charge_count=models.CharField(null=False,max_length=254)
#     收费金额
    charge_date=models.DateField(null=False)
#     收费开始日期
    charge_infor=models.CharField(null=False,max_length=254)
#     收费的介绍


# --------------------------收费项目------------------------


# ---------------------------















