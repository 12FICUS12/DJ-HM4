from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teachers').order_by('group')  # Загружаем всех студентов и их учителей, упорядочивая по полю "group"
    context = {'students': students}

    return render(request, template, context)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by



