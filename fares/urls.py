from django.urls import path

from . import views
from fares.views import LegRuleListView, LegRuleListFilteredView, TransferListView

urlpatterns = [
    path('', views.index, name='index'),
    path('rider/<int:rider_id>', views.rider, name='rider_detail'),
    path("legrulelist", LegRuleListView.as_view(), name='legrule_list'),
    path("transferlist", TransferListView.as_view(), name='transfer_list'),
    path("legrulelistfiltered", LegRuleListFilteredView.as_view(), name='legrule_filtered_list')
    
]