from django import forms
from .models import Contact
from .models import Contact, Blog, Category
from django.forms import ModelChoiceField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField


class NameChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.category_name}'

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
    description = forms.CharField(widget=CKEditorWidget())
    images = forms.FileField(required=False),
    category= NameChoiceField(queryset=Category.objects.filter(is_available=True).order_by('category_name'), required=True)
    class Meta:
        model = Blog
        exclude = ('slug','is_available')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'name': forms.TextInput(attrs={'value': '', 'class':'form-control'}),
            'image_url': forms.Textarea(attrs={'class': 'form-control'}),
            
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }