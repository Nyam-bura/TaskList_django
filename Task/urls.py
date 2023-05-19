from django.urls import path
from Task import views
urlpatterns=[
        path('login/',views.LoginApiView.as_view(), name='login'),
        path('signup/',views.SignUpApiView.as_view(),name='signup')   
]

