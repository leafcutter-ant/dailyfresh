from django.db import models
from dbmodel.base_model import BaseModel
from dbmodel.encryption import Encrytion


class UserAccountManager(models.Manager):

    def addUser(self,username,password,email):
        className = self.model
        # sha1加密密码后存入数据库
        password = Encrytion.sha1(password)
        obj = className(username=username,password=password,email=email)
        obj.save()
        return obj

    def findUserByName(self,username):
        print('find name')
        className = self.model
        objs = className.objects.filter(username=username)
        if objs is None or len(objs) == 0:
            return False
        else:
            return True

    def findUserByName_pwd(self,username,pwd):
        className = self.model
        pwd = Encrytion.sha1(pwd)
        obj = className.objects.filter(username=username,password=pwd)
        if obj is None or len(obj) == 0:
            return None
        else:
            return obj


class UserAccount(BaseModel):
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=40,verbose_name='密码')
    email = models.EmailField(verbose_name='用户邮箱')

    objects = UserAccountManager()  # 管理器类

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_account'


if __name__ == '__main__':
    res = UserAccount.objects.findUserByName_pwd('python','asdfasdf')
    print(res)
