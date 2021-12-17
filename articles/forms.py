from django.forms import ModelForm, fields
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields=['titre','contenu','slug','images']