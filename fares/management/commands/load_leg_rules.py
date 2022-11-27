import csv
from django.core.management import BaseCommand
from fares.models import Leg_Rule, Rider_Category, Area, Fare_Container, Network

class Command(BaseCommand):
    help = 'Load leg_rules from csv'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                Question.objects.create(
                    attr1=row[0],
                    attr2=row[1],
                )
            
