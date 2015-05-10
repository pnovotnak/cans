from django.db import models


class NamedModel(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Artist(NamedModel):

    description = models.TextField()
    image = models.ImageField(upload_to='artist_images', blank=True, null=True)


class ReleaseGroup(NamedModel):

    artist = models.ForeignKey('Artist')


class Release(NamedModel):

    year = models.DateField()
    image = models.ImageField(blank=True, null=True)
    release_group = models.ForeignKey('ReleaseGroup')

    def __str__(self):
        return self.release_group.name + ' (' + self.name + ')'


class Track(NamedModel):

    release = models.ManyToManyField('Release')
    number = models.SmallIntegerField()
    length = models.SmallIntegerField()

    def human_length(self):
        return str(self.length / 60) + ':' + str(self.length % 60).zfill(2)

    class Meta:
        ordering = ('-number', 'name')
