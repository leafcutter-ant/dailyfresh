from django.shortcuts import render
from .models import UserAccount
from django.http import HttpResponse,JsonResponse
import hashlib

def register(res):
    return render(res,'user_module/register.html')

def register_handler(res):
    args = res.POST
    username = args.get('user_name')
    password = args.get('pwd')
    email = args.get('email')

    obj = UserAccount.objects.addUser(username,password,email)

    # return HttpResponse('register ok name:'+obj.username)
    return render(res,'user_module/login.html')


def login(res):
    return render(res, 'user_module/login.html')


# 处理前端的ajax提交的 验证用户名是否重复的函数
def check_name(res):
    name = res.GET.get('username')
    res = UserAccount.objects.findUserByName(name)
    if not res:
        # 找到此昵称用户
        return JsonResponse({'res':1 })
    else:
        return JsonResponse({'res':0 })


# 处理登录请求的函数
def login_handler(res):
    args = res.POST
    username = args.get('username')
    password = args.get('pwd')

    user = UserAccount.objects.findUserByName_pwd(username,password)
    if user is not None:
        return render(res,'user_module/index.html')
    else:
        print(user)
        return HttpResponse('not find user')




