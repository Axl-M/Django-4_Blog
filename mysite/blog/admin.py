from django.contrib import admin
from .models import Post
# Register your models here.


# admin.site.register(Post)

# изменить внешний вид отображения модели на сайте администрирования
@admin.register(Post)   # тоже что и  admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}  # При вводе заголовка нового поста поле slug заполнять автоматически
    raw_id_fields = ['author']  # выбор автора отображать поисковым виджетом (а не выпадающим списком)
    date_hierarchy = 'publish'  # навигации по иерархии дат
    ordering = ['status', 'publish']  # по умолчанию посты упорядочены по столбцам (Статус) и (Опубликован)