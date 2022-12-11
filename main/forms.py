from django import forms
from .models import Contact
from .models import Contact, Blog
# from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ("first_name", "last_name", "e_mail")
        # exclude = ("first_name",)

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập Tên Của Bạn'}),
            "e_mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ email'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}),
            "subject": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiêu đề'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'message'})
        }

class CreateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=RichTextUploadingField())
    class Meta:
        model = Blog
        exclude = ('slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'name': forms.TextInput(attrs={'value': '', 'class':'form-control'}),
            'images': forms.FileUpload(attrs={'value': ''}),
            'image_url': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'value': '','id':'Category' ,'class':'form-control'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }