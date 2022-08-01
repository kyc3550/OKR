from django import forms
from .models import Board

class WriteForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        required=True,
        widget = forms.TextInput(
            attrs = {
                'class' : "form-control"
            }
        ),
    )
    contents = forms.CharField(
        label = '내용',
        required=True,
        widget = forms.Textarea(
            attrs = {
                'class' : "form-control",
                'rows' : 17,
                
            }
        ),
    )
    photo = forms.ImageField(
        label = '사진',
    )

    class Meta:
        model = Board
        fields = ['title','contents','photo']
    
    def clean(self):
        cleand_data = super().clean()

        title = cleand_data.get('title','')
        contents = cleand_data.get('contents','')
        photo = cleand_data.get('photo','')
        if title == '':
            self.add_error('title','글 제목을 입력하세요.')
        if contents == '':
            self.add_error('contents','글 내용을 입력하세요.')
        else:
            self.title = title
            self.contents = contents
            self.photo = photo