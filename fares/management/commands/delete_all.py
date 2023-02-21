import csv
from django.db import models
from django.core.management import BaseCommand
from fares.models import *


class Command(BaseCommand):
    help = 'Deletes all objects'

    def handle(self, *args, **kwargs):
        Transfer_Rule.objects.all().delete()
        Leg_Rule.objects.all().delete()
        Leg_Group.objects.all().delete()

        Product.objects.all().delete()

        Stop_Area.objects.all().delete()
        Area.objects.all().delete()
        Stop.objects.all().delete()
        Network.objects.all().delete()
        Route.objects.all().delete()

        Rider_Category.objects.all().delete()
        Fare_Container.objects.all().delete()
        Calendar.objects.all().delete()
