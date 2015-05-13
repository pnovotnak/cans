from django.db import models


class NamedModel(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Queue(models.Model):
    """ A basic task queue.

    Tasks are given a priority between 1 (highest) and 10 (lowest)
    """

    priority_choices = zip(range(1, 10), range(1, 10))

    action = models.TextField()
    priority = models.SmallIntegerField(default=5, choices=priority_choices)


class Artist(NamedModel):

    description = models.TextField()
    image = models.ImageField(upload_to='artist_images', blank=True, null=True)
    mbid = models.CharField(max_length=255)  # MusicBrainz id


class ReleaseGroup(NamedModel):

    artist = models.ForeignKey('Artist')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)


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
