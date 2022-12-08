import csv
from django.db import models
from django.core.management import BaseCommand
from fares.models import * 
from fares.resources import ProductResource
from import_export.formats import base_formats
import os
from faresDjango.settings import BASE_DIR
from import_export.admin import ImportMixin


FORMATS = {
    'text/csv': base_formats.CSV,
}
format_number = 0  # CSV

class Command(BaseCommand):
    help = 'Load product from csv using django import export'
   
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        data_dir =  os.path.join(BASE_DIR, 'fares/data_in/')
        import_file_name = os.path.join(data_dir, 'fare_products.txt')
        print(import_file_name)
        
        mixin = ImportMixin()
        input_format = mixin.get_import_formats()[format_number]()
        import_file = open(import_file_name, input_format.get_read_mode())
        dataset = input_format.create_dataset(import_file)
        resource = ProductResource()
        resource.import_data(dataset, dry_run=False, raise_errors=True, file_name=import_file_name)
        import_file.close()
   
     