from django.db import models
from django.contrib.auth.models import User

class Monster(models.Model):
    monster_type = models.CharField(max_length=255)
    monster_name = models.CharField(max_length=255, null=True, blank=True)
    monster_details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.monster_type

    class Meta:
        db_table = 'monster'
        verbose_name_plural = 'monsters'

class Sighting(models.Model):
    which_monster = models.ForeignKey(Monster, on_delete=models.DO_NOTHING)
    when = models.DateField()
    where = models.CharField(max_length=255)
    who = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return 'Monster Sighting #: ' + str(self.id)

    class Meta:
        db_table = 'sighting'
        verbose_name_plural = 'sightings'