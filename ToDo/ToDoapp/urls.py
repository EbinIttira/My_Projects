from django . urls import path
from .import views
app_name='ToDoapp'
urlpatterns=[
path('listview/',views.TaskListview.as_view(),name='listview'),
path('detailview/<int:pk>/',views.TaskDetailview.as_view(),name='detailview'),
path('updateview/<int:pk>/',views.TaskUpdateview.as_view(),name='updateview'),
path('deleteview/<int:pk>/',views.TaskDeleteview.as_view(),name='deleteview'),
path('',views.addtask,name='addtask'),
path('delete/<int:id>/',views.delete,name='delete'),
path('update/<int:id>/',views.update,name='update'),
]
