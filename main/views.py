from .models import AboutUs, News, Scientist, ScientistEbooks, ScientistAudio, ScientistMovie, ScientistFotoGallery, \
    Test
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class AboutUsAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = serializers.AboutSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class ScientistListAPIView(generics.ListAPIView):
    queryset = Scientist.objects.all()
    serializer_class = serializers.ScientistSerializer


class ScientistDetailAPIView(generics.RetrieveAPIView):
    queryset = Scientist.objects.all()
    serializer_class = serializers.ScientistSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        obj = Scientist.objects.get(id=self.kwargs.get('pk'))
        obj.views += 1
        obj.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ScientistMovieAPIView(generics.ListAPIView):
    serializer_class = serializers.ScientistMovieSerializer

    def get_queryset(self):
        queryset = ScientistMovie.objects.all()
        pk = self.request.GET.get('scientist_id')
        if pk:
            queryset = queryset.filter(scientist_id=pk)
        return queryset


class ScientistAudioListAPIView(generics.ListAPIView):
    serializer_class = serializers.ScientistAudioSerializer

    def get_queryset(self):
        queryset = ScientistAudio.objects.all()
        pk = self.request.GET.get('scientist_id')
        if pk:
            queryset = queryset.filter(scientist_id=pk)
        return queryset


class ScientistFotoAPIView(generics.ListAPIView):
    serializer_class = serializers.ScientistFotoGallerySerializers

    def get_queryset(self):
        queryset = ScientistFotoGallery.objects.all()
        pk = self.request.GET.get('scientist_id')
        if pk:
            queryset = queryset.filter(scientist_id=pk)
        return queryset


class ScientistEbookListAPIView(generics.ListAPIView):
    serializer_class = serializers.ScientistEbooksSerializer

    def get_queryset(self):
        queryset = ScientistEbooks.objects.all()
        pk = self.request.GET.get('scientist_id')
        if pk:
            queryset = queryset.filter(scientist_id=pk)
        return queryset


class TestListAPIView(generics.ListAPIView):
    queryset = Test.objects.all().order_by('?')[:10]
    serializer_class = serializers.TestSerializer
