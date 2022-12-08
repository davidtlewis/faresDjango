import csv
from django.db import models
from django.core.management import BaseCommand
from fares.models import * 
from fares.resources import *
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
    data_dir =  os.path.join(BASE_DIR, 'fares/data_in/')
    
    def handle(self, *args, **kwargs):
        
   
        def import_file(import_file_name, ResourceClass):
            data_dir =  os.path.join(BASE_DIR, 'fares/data_in/')
            import_file_name = os.path.join(data_dir, import_file_name)
            print(f"Processing: {import_file_name}")
            mixin = ImportMixin()
            input_format = mixin.get_import_formats()[format_number]()
            import_file = open(import_file_name, input_format.get_read_mode())
            dataset = input_format.create_dataset(import_file)
            resource = ResourceClass()
            resource.import_data(dataset, dry_run=False, raise_errors=True, file_name=import_file_name)
            import_file.close() 

        import_file('fare_products.txt',ProductResource)
        import_file('fare_leg_rules.txt',LegRuleResource)