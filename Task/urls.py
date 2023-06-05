from django.urls import path
from Task import views
urlpatterns=[
        path('login/',views.LoginApiView.as_view(), name='login'),
        path('signup/',views.SignUpApiView.as_view(),name='signup'),
        path('task/',views.TaskApiView.as_view(),name="task") ,
        path('subtask/',views.SubTaskApiView.as_view(),name='subtask'),
        # path('subtasks/',views.AddSubTaskApiView.as_view(),name='subtasks')
        # path('data/',views.DataApiview.as_view(),name='data')
]

