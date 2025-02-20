from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {
        'object_list': Article.objects.all().order_by(ordering),
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
