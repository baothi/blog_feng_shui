from django import forms
from .models import ProductComment
from django.forms import ModelChoiceField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = "__all__"
        # fields = ("first_name", "last_name", "e_mail")
        # exclude = ("first_name",)

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập Tên Của Bạn'}),
            "e_mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ email'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}),
            "subject": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiêu đề'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'message'}),
            "product": forms.TextInput(attrs={'value': '', 'id':'product', 'type':'hidden'}),
        }