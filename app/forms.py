# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/4/27  12:38


from django import forms
from django.forms import widgets
from app import models
from django.core.exceptions import ValidationError
import re


class UserForm(forms.Form):
    username=forms.CharField(max_length=32,
                         label='用户名',
                         error_messages={'required':'不能为空'},
                         widget=widgets.TextInput(attrs={},)
                         )

    # pwd = forms.CharField(max_length=32,
    #                        label='密码',
    #                        error_messages={'required': '不能为空'},
    #                        widget=widgets.PasswordInput(attrs={}, )
    #                        )
    #
    # re_pwd = forms.CharField(max_length=32,
    #                        label='确认密码',
    #                        error_messages={'required': '不能为空'},
    #                        widget=widgets.PasswordInput(attrs={}, )
    #                        )

    email = forms.EmailField(
        required=False,
        error_messages={'invalid': u'请输入正确的邮箱'}
    )
    telphone = forms.CharField(required=False,
                               max_length=11,
                               error_messages={'max_length': '手机号超过11个号码'},
                               )

    def clean_telphone(self):
        tel=self.cleaned_data.get('telphone')
        if tel:
            ret = re.match(r"^1[35678]\d{9}$", tel)
            if ret:
                return tel
            else:
                raise ValidationError('手机格式不正确')

    # def clean_user(self):
    #     val = self.cleaned_data.get('user')
    #     user = models.User.objects.filter(username=val).first()
    #     if not user:
    #         return val
    #     else:
    #         raise ValidationError('该用户已注册！')
    #
    # def clean(self):
    #     pwd=self.cleaned_data.get('pwd')
    #     re_pwd=self.cleaned_data.get('re_pwd')
    #     if pwd and re_pwd:
    #         if pwd==re_pwd:
    #             return self.cleaned_data
    #         else:
    #             raise ValidationError('两次输入密码不一样！')
    #     else:
    #         return self.cleaned_data
