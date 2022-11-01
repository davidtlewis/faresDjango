from django.urls import path

from . import views
from fares.views import LegRuleListView, LegRuleListFilteredView

urlpatterns = [
    path('', views.index, name='index'),
    path('rider/<int:rider_id>', views.rider, name='rider_detail'),
    path("legrulelist", LegRuleListView.as_view()),
    path("legrulelistfiltered", LegRuleListFilteredView.as_view())
    
]