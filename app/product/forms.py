from django import forms
from .models import Category

class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)
        
        if 'parent' in self.fields:
            self.fields['parent'].queryset = Category.objects.filter(is_parent=True)