# My working codes

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup_view, name='signup'),
#     path('profile/', views.profile_view, name='profile'),
# ]


from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
		path('', views.index, name ='index'),
]
