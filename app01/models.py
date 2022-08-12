from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    #
    # size = models.IntegerField(default=2)
    # data = models.IntegerField(null=True, blank=True)


class Department(models.Model):
    title = models.CharField(max_length=32)

# ######新增数据######
# 新建数据 inser into app01_department(title) values("销售部")
# Department.objects.create(title="销售部")

# ######删除数据######
# Department.objects.filter(id=3).delete()
# Department.objects.all().delete()

# ######查询数据######
# Department.objects.all() 返回QuerySet类型
# Department.objects.filter(id=1) 返回QuerySet类型

# ######更新数据######
# Department.objects.all().update(title="****")
# Department.objects.filter(id=1).update(title="*****")
