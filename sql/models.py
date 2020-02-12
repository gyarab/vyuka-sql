from django.db import models


class Battle(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()

class ShipClass(models.Model):
    name = models.CharField(max_length=50)
    typ = models.CharField(max_length=2)
    country = models.CharField(max_length=20)
    numGuns = models.IntegerField()
    bore = models.FloatField()
    displacement = models.IntegerField()

class Ship(models.Model):
    name = models.CharField(max_length=50)
    cls = models.ForeignKey(ShipClass, on_delete=models.CASCADE)
    launched = models.IntegerField()

class Outcome(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=10)
