from rest_framework import serializers
from .models import AboutUs, News, Scientist, ScientistEbooks, ScientistAudio, ScientistMovie, ScientistFotoGallery, \
    Test, NewsImage


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['name', 'sub_title', 'about_us']


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['id', 'image']


class NewsSerializer(serializers.ModelSerializer):
    news_images = NewsImageSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'created_at', 'news_images']


class ScientistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientist
        fields = ['id', 'date_birth', 'views', 'name', 'image', 'biography']


class ScientistMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientistMovie
        fields = ['id', 'name', 'link_video']


class ScientistAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientistAudio
        fields = ['id', 'name', 'image', 'audio']


class ScientistFotoGallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = ScientistFotoGallery
        fields = ['id', 'image']


class ScientistEbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientistEbooks
        fields = ['id', 'name', 'file']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'question', 'answer_1', 'answer_2', 'answer_3', 'answer_true']
