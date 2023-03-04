from django_filters import FilterSet, ModelChoiceFilter
from .models import Post


class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'typ': ['exact'],
           'time': ['gt'],
       }
