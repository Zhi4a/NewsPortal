from django.urls import path
from .views import *


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),

   path('news/edit/', NewsCreate.as_view(), name='news_edit'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

   path('articles/edit/', ArticlesCreate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),

   path('<int:pk>/subscribe/', subscribe, name='subscribe'),
   path('<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]
