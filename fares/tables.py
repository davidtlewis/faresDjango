# tutorial/tables.py
import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
# from .models import Leg_Rule, Transfer_Rule
from .models import *


class LegRuleTable(tables.Table):
    productName = tables.Column(
        accessor='product.name', verbose_name='Prod Name')
    productAmount = tables.Column(
        accessor='product.amount', verbose_name='Prod Amount')
    from_area = tables.LinkColumn("area_stops_filtered_list")
    to_area = tables.LinkColumn("area_stops_filtered_list")
    network = tables.LinkColumn("route_filtered_list")

    class Meta:
        model = Leg_Rule
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "network", "from_area", "to_area", "rider_category",
                  "fare_container", "service_id", "amount", "leg_group", "productName", "productAmount")

    def render_from_area(self, record):
        url = reverse('area_stops_filtered_list')
        return format_html('<a href="{}?area_id={}">{}</a>', url, record.from_area.id, record.from_area)

    def render_to_area(self, record):
        url = reverse('area_stops_filtered_list')
        return format_html('<a href="{}?area_id={}">{}</a>', url, record.to_area.id, record.to_area)

    def render_network(self, record):
        url = reverse('route_filtered_list')
        return format_html('<a href="{}?network_id={}">{}</a>', url, record.network.id, record.network)


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


class AreaStopsTable(tables.Table):
    stop_name = tables.Column(accessor='stop_id.stop_name')
    location_type = tables.Column(accessor='stop_id.location_type')

    class Meta:
        model = Stop_Area
        template_name = "django_tables2/bootstrap.html"


class StopTable(tables.Table):
    class Meta:
        model = Stop
        template_name = "django_tables2/bootstrap.html"


class RouteTable(tables.Table):
    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap.html"


class FareContainerTable(tables.Table):
    class Meta:
        model = Fare_Container
        template_name = "django_tables2/bootstrap.html"


class CalendarTable(tables.Table):
    class Meta:
        model = Calendar
        template_name = "django_tables2/bootstrap.html"
