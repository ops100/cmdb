#!/usr/bin/env python3
# coding:utf-8
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Register(forms.Form):
    username = forms.CharField(
        min_length=1,
        label="用户名",
        error_messages={
            "required": "不能为空",
            "min_length": "用户名最少1位"
        },
        widget=forms.widgets.TextInput(attrs={"class": "fas fa-user", "placeholder": "用户名","autocomplete":"off"})
    )
    password = forms.CharField(
        min_length=1,
        label="密码",
        error_messages={
            "required": "不能为空",
            "min_length": "密码最少1位"
        },
        widget=forms.widgets.PasswordInput(
            attrs={"class": "fas fa-user", "plaaceholder": "密码","autocomplete":"off"},
            render_value=True
        )
    )
    re_password = forms.CharField(
        min_length=1,
        label="确认密码",
        error_messages={
            "required": "不能为空",
            "min_length": "密码最少1位"
        },
        widget=forms.widgets.PasswordInput(
            attrs={"class": "fas fa-user", "placeholder": "确认密码","autocomplete":"off"},
            render_value=True
        )
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            self.add_error("re_password", "两次输入的密码不一致！")
        else:
            return self.cleaned_data

class Login(forms.Form):
    username = forms.CharField(
        min_length=1,
        label="用户名",
        error_messages={
            "required": "不能为空",
            "min_length": "用户名最少1位"
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名","autocomplete":"off"})
    )
    password = forms.CharField(
        min_length=1,
        label="密码",
        error_messages={
            "required": "不能为空",
            "min_length": "密码最少1位"
        },
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control", "plaaceholder": "密码","autocomplete":"off"},
            render_value=True
        )
    )

