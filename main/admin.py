from django.contrib.admin import register, StackedInline
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import News, AboutUs, Scientist, ScientistEbooks, ScientistAudio, ScientistMovie, ScientistFotoGallery, \
    Test, NewsImage


class NewsImageAdmin(StackedInline):
    model = NewsImage
    extra = 1


@register(News)
class NewsAdmin(TranslationAdmin):
    inlines = [NewsImageAdmin]


@register(AboutUs)
class AboutAdmin(TranslationAdmin):
    pass


class ScientistEbookAdmin(TranslationStackedInline):
    model = ScientistEbooks
    extra = 1


class ScientistMovieAdmin(TranslationStackedInline):
    model = ScientistMovie
    extra = 1


class ScientistAudioAdmin(TranslationStackedInline):
    model = ScientistAudio
    extra = 1


class ScientistFotoAdmin(StackedInline):
    model = ScientistFotoGallery
    extra = 1


@register(Scientist)
class ScientistAdmin(TranslationAdmin):
    inlines = [ScientistFotoAdmin, ScientistAudioAdmin, ScientistEbookAdmin, ScientistMovieAdmin]


@register(Test)
class TestAdmin(TranslationAdmin):
    pass
