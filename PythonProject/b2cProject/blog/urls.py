from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path(url,view,template django template tag url name)
    #In blog/urls.py we created a URL rule named post_detail that refers to a view called views.post_detail. 
    # This means that Django will be expecting a view function called post_detail inside blog/views.py.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/<int:test>/edit/', views.post_edit_viewname, name='post_edit_urlname'),
]