from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('schedule/', views.schedule_page, name='schedule_page'),
    path('add-employee/', views.add_employee, name='add_employee'),  # ← ДОБАВЬ ЭТУ СТРОЧКУ
]