# staff/views.py
from django.shortcuts import render, redirect
from .forms import EmployeeForm

# Наши сотрудники - ЧИСТЫЕ ДАННЫЕ
users = [
    {
        'name': 'Смирнова Мария Михайловна',
        'phone': '8(495)344-99-33',
        'email': 'smimova@gmail.com',
        'position': 'менеджер'
    },
    {
        'name': 'Иванов Иван Иванович',
        'phone': '8(495)123-45-67',
        'email': 'ivanov@gmail.com',
        'position': 'разработчик'
    },
    {
        'name': 'Петрова Анна Сергеевna',
        'phone': '8(495)765-43-21',
        'email': 'petrova@gmail.com',
        'position': 'дизайнер'
    }
]


def employee_list(request):
    global users

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Добавляем нового сотрудника
            new_user = {
                'name': form.cleaned_data['full_name'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'position': form.cleaned_data['position']
            }

            users.append(new_user)
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'staff/employee_list.html', {
        'users': users,  # передаем users в шаблон
        'form': form
    })


def schedule_page(request):
    return render(request, 'staff/schedule.html')


def add_employee(request):
    global users

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Добавляем нового сотрудника
            new_user = {
                'name': form.cleaned_data['full_name'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'position': form.cleaned_data['position']
            }

            users.append(new_user)
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'staff/add_employee.html', {'form': form})