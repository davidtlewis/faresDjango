# tutorial/tables.py
import django_tables2 as tables
# from .models import Leg_Rule, Transfer_Rule
from .models import *


class LegRuleTable(tables.Table):
    productName = tables.Column(accessor='product.name')
    productAmount = tables.Column(accessor='product.amount')
    class Meta:
        model = Leg_Rule
        template_name = "django_tables2/bootstrap.html"
        fields = ("id","network", "from_area","to_area","rider_category","fare_container", "leg_group","productName","productAmount" )

class RiderTable(tables.Table):
    class Meta:
        model = Rider_Category
        template_name = "django_tables2/bootstrap.html"

class TransferTable(tables.Table):
    class Meta:
        model = Transfer_Rule
        template_name = "django_tables2/bootstrap.html"

class NetworkTable(tables.Table):
    class Meta:
        model = Network
        template_name = "django_tables2/bootstrap.html"

class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap.html"

class AreaTable(tables.Table):
    class Meta:
        model = Area
        template_name = "django_tables2/bootstrap.html"

