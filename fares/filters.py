import django_filters
from fares.models import *

class LegRuleFilter(django_filters.FilterSet):
    # from_area = django_filters.CharFilter(field_name='from_area__ref_id', lookup_expr='icontains')
    network = django_filters.ModelChoiceFilter(queryset=Network.objects.all(), empty_label="Network" )
    from_area = django_filters.ModelChoiceFilter(queryset=Area.objects.all(), empty_label="From Area" )
    to_area = django_filters.ModelChoiceFilter(queryset=Area.objects.all(), empty_label="To Area" )
    fare_container  = django_filters.ModelChoiceFilter(queryset=Fare_Container.objects.all(), empty_label="Container" )
    rider_category  = django_filters.ModelChoiceFilter(queryset=Rider_Category.objects.all(), empty_label="Rider" )

    class Meta:
        model = Leg_Rule
        fields = ['network','from_area','to_area','fare_container','rider_category']
        # fields = ['from_area', 'to_area']


class RouteFilter(django_filters.FilterSet):
    network_id = django_filters.ModelChoiceFilter(queryset=Network.objects.all(), empty_label="Network" )
    class Meta:
        model = Route
        fields = ['network_id',]

class AreaStopsFilter(django_filters.FilterSet):
    area_id = django_filters.ModelChoiceFilter(queryset=Area.objects.all(), empty_label="Area" )
    class Meta:
        model = Stop_Area
        fields = ['area_id',]