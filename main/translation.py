from .models import AboutUs, Scientist, ScientistAudio, ScientistMovie, ScientistEbooks, News, \
    Test
from modeltranslation.translator import register, TranslationOptions


@register(AboutUs)
class AboutTrans(TranslationOptions):
    fields = ('name', 'sub_title', 'about_us')


@register(News)
class NewsTrans(TranslationOptions):
    fields = ('title', 'content')


@register(Scientist)
class ScientistTrans(TranslationOptions):
    fields = ('name', 'biography')


@register(ScientistMovie)
class ScientistMovieTrans(TranslationOptions):
    fields = ('name',)


@register(ScientistAudio)
class ScientistFoto(TranslationOptions):
    fields = ('name',)


@register(ScientistEbooks)
class Ebook(TranslationOptions):
    fields = ('name',)


@register(Test)
class TestTrans(TranslationOptions):
    fields = ('question', 'answer_1', 'answer_2', 'answer_3', 'answer_true')
