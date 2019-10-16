from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


class CategoriesInline(admin.StackedInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInline
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
