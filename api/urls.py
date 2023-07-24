from django.urls import path
from .views import get_all,get_by_id,create,update,delete,lookname,lookgt,lookrange,looklte

urlpatterns = [
    path('products/all/', get_all),
    path('products/<int:pk>/get', get_by_id),
    path('products/<int:pk>/update',update),
    path('products/create',create),
    path('products/<int:pk>/delete', delete),
    path('products/<str:str>/getname',lookname),
    path('products/<int:pk>/getgt',lookgt),
    path('products/<int:pk>/getlte',looklte),
    path('products/<int:min>&<int:max>/getrange',lookrange)


]