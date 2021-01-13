#!/usr/bin/env python3
#coding:utf-8
import json
from datetime import datetime

from decimal import Decimal
from django.db.models import QuerySet

# 日期json序列化
from django.shortcuts import redirect


# 转换时间格式到字符串
def human_datetime(date=None):
    if date:
        assert isinstance(date, datetime)
    else:
        date = datetime.now()
    return date.strftime('%Y-%m-%d %H:%M:%S')





# 自定义登录验证装饰器
def check_login(func):  # 自定义登录验证装饰器
    def warpper(request, *args, **kwargs):
        is_login = request.session.get('is_login', False)
        if is_login:
            func(request, *args, **kwargs)
        else:
            return redirect("/login")
    return warpper