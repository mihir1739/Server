from MiPIS import views 

from django.urls import path 

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('logout/', views.user_logout, name="logout"),
    path('data/',views.database,name='database'),
    path('submit/<int:id>',views.update),
    path('approve/',views.approve,name='approve'),
    path('approveme/<int:id>',views.foundem,name='approve me')
]