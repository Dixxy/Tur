from modeltranslation.translator import register, TranslationOptions

from tours.models import TourTagModel, TourModel


@register(TourTagModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TourModel)
class CommentModelOptions(TranslationOptions):
    fields = ('title', 'long_description',)
