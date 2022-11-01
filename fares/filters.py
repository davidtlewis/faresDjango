import django_filters
from fares.models import Leg_Rule, Rider_Category

class LegRuleFilter(django_filters.FilterSet):
    class Meta:
        model = Leg_Rule
        fields = ['network','from_area','to_area','fare_container','rider_category']