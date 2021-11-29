from modeltranslation.translator import register, TranslationOptions

from posts.models import PostModel, CommentModel


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'banner',)


@register(CommentModel)
class CommentModelOptions(TranslationOptions):
    fields = ('comment',)
