#!/usr/bin/env python3
#coding:utf-8
import json
from datetime import datetime, date as datetime_date
from decimal import Decimal
from django.db.models import QuerySet

# 日期json序列化
from django.shortcuts import redirect


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime_date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, Decimal):
            return float(o)

        return json.JSONEncoder.default(self, o)

# 自定义登录验证装饰器
def check_login(func):  # 自定义登录验证装饰器
    def warpper(request, *args, **kwargs):
        is_login = request.session.get('is_login', False)
        if is_login:
            func(request, *args, **kwargs)
        else:
            return redirect("/login")
    return warpper