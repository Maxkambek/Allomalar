from django.db import models


class AboutUs(models.Model):
    name = models.CharField(max_length=221, verbose_name='Nomi')
    sub_title = models.TextField(verbose_name="Qo'shimcha sarlavha")
    about_us = models.TextField(verbose_name='Matn')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizda'


class News(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=222, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Mazmuni')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Yangiliklar'


class NewsImage(models.Model):
    image = models.ImageField(upload_to='news/')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_images')


class Scientist(models.Model):
    name = models.CharField(max_length=221, verbose_name='Ismi')
    date_birth = models.CharField(max_length=50, verbose_name="Hayoti:tug'ilgan va vafot etgan yili")
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='scientists/')
    biography = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Allomalar'
        verbose_name_plural = 'Allomalar'


class ScientistMovie(models.Model):
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    link_video = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Filmlar'
        verbose_name_plural = 'Filmlar'


class ScientistAudio(models.Model):
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    name = models.CharField(max_length=222)
    image = models.ImageField(upload_to='audio_images/')
    audio = models.FileField(upload_to='audio_files/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Audiolavhalar'
        verbose_name_plural = 'Audiolavhalar'


class ScientistFotoGallery(models.Model):
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fotogallery/')

    class Meta:
        verbose_name = 'FotoGalareya'
        verbose_name_plural = 'FotoGalareya'


class ScientistEbooks(models.Model):
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    file = models.FileField(upload_to='e-books/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Elektron Kitoblar'
        verbose_name_plural = 'Elektron Kitoblar'


class Test(models.Model):
    question = models.CharField(max_length=1000, verbose_name='Savol')
    answer_1 = models.CharField(max_length=1000, verbose_name="Javob 1")
    answer_2 = models.CharField(max_length=1000, verbose_name="Javob 2")
    answer_3 = models.CharField(max_length=1000, verbose_name="Javob 3")
    answer_true = models.CharField(max_length=1000, verbose_name="To'g'ri Javob")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Test'
