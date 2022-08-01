from django import forms
from .models import User
from argon2 import PasswordHasher, exceptions
from django.forms import ModelForm,TextInput,PasswordInput

GENDER_CHOICES = (
    (0, '여자'),
    (1, '남자'),
    )

class RegisterForm(ModelForm):
    
    user_name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        ),
        error_messages={'required' : '이름를 입력해 주세요.'}
    )
    user_id = forms.CharField(
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        ),
        error_messages={'required' : '아이디를 입력해 주세요.'}
    )
    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control"
            }
        ),
        error_messages={'required' : '비밀번호를 입력해 주세요.'}
    )
    user_pw_confirm = forms.CharField(
        label='비밀번호 재입력',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control"
            }
        ),
        error_messages={'required': '비밀번호를 입력해 주세요.'}
    )
    user_phone_number = forms.CharField(
        label='핸드폰 번호',
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        ),
        error_messages={'required': '전화번호를 입력해 주세요.'}
    )
    user_gender = forms.ChoiceField(
        label='성별',
        choices = GENDER_CHOICES,
    )
    class Meta:
        model = User
        fields = ['user_id','user_name','user_pw','user_pw_confirm','user_phone_number','user_gender',]
        
    def clean(self):
        cleand_data = super().clean()

        user_name = cleand_data.get('user_name','')
        user_id = cleand_data.get('user_id','')
        user_pw = cleand_data.get('user_pw','')
        user_pw_confirm = cleand_data.get('user_pw_confirm','')
        user_phone_number = cleand_data.get('user_phone_number','')
        user_gender = cleand_data.get('user_gender','')

        if user_pw != user_pw_confirm:
            return self.add_error('user_pw_comfirm','비밀번호가 다릅니다.')
        elif not(4<=len(user_id) <= 16):
            return self.add_error('user_id','아이디는 4~16자로 입력해 주세요')
        else:
            self.user_id = user_id
            self.user_pw = PasswordHasher().hash(user_pw)
            self.user_pw_confirm = user_pw_confirm
            self.user_name = user_name
            self.user_phone_number = user_phone_number
            self.user_gender = user_gender

class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length = 32,
        label = '아이디',
        required = True,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        ),
        error_messages = {'required' : '아이디를 입력해주세요.'}
    )
    user_pw = forms.CharField(
        max_length = 128,
        label = '비밀번호',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class' : 'form-control',
            }
        ),
        error_messages = {'required' : '비밀번호를 입력해주세요.'}
        
    )
    
    field_order = ['user_id', 'user_pw']

    def clean(self):
        cleand_data = super().clean()

        user_id = cleand_data.get('user_id','')
        user_pw = cleand_data.get('user_pw','')
        
        if user_id == '':
            return self.add_error('user_id','아이디를 다시 입력해 주세요.')
        elif user_pw =='':
            return self.add_error('user_pw','비밀번호를 다시 입력해 주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id', '아이디가 존재하지 않습니다.')
            
            try:
                PasswordHasher().verify(user.user_pw,user_pw)
            except exceptions.VerifyMismatchError:
                return self.add_error('user_pw','비밀번호가 다릅니다.')
            self.login_session = user.user_id