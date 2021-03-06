from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from tours.models import TourModel, TourTagModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
              'http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery-ui.min.js',
              'modeltranslation/js/tabbed_translation_fields.js',
              )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(TourModel)
class TourModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'long_description', 'img1', 'price', 'discount']
    list_filter = ['price']
    search_fields = ['title', 'discount', 'message', 'created_at']


@admin.register(TourTagModel)
class ProductTagModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']

# @admin.register(CategoryModel)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_at']
#     search_fields = ['title']
#     list_filter = ['created_at']
