from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Teg, ArticleTeg


@admin.register(Teg)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ArticleTegsFormSet(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Выберите хотя бы один тег')

        has_is_main_tag = False
        is_main_tag_count = 0

        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                has_is_main_tag = True
                is_main_tag_count += 1

        if not has_is_main_tag:
            raise ValidationError('Выберите хотя бы один тег основным')

        if is_main_tag_count > 1:
            raise ValidationError('Может быть только один основной тег')

        return super().clean()

class ArticleTegInline(admin.TabularInline):
    model = ArticleTeg
    extra = 1
    formset = ArticleTegsFormSet

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'published_at', 'image')
    inlines = [ArticleTegInline]






