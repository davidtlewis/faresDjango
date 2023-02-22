from django.urls import path

from . import views
# from fares.views import LegRuleListView, LegRuleListFilteredView, TransferListView, RiderListView, NetworkListView, ProductListView, FareContainerListView
from fares.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('rider/<int:rider_id>', views.rider, name='rider_detail'),
    path("legrulelist", LegRuleListView.as_view(), name='legrule_list'),
    path("transferlist", TransferListView.as_view(), name='transfer_list'),
    path("legrulelistfiltered", LegRuleListFilteredView.as_view(),
         name='legrule_filtered_list'),
    path("transferlist", TransferListView.as_view(), name='transfer_list'),
    path("riderlist", RiderListView.as_view(), name='rider_list'),
    path("networklist", NetworkListView.as_view(), name='network_list'),
    path("productlist", ProductListView.as_view(), name='product_list'),
    path("farecontainerlist", FareContainerListView.as_view(),
         name='farecontainer_list'),
    path('arealist', AreaListView.as_view(), name='area_list'),
    path('stoplist', StopListView.as_view(), name='stop_list'),
    path('routelist', RouteListView.as_view(), name='route_list'),
    path('calendarlist', CalendarListView.as_view(), name='calendar_list'),
    path("routelistfiltered", RouteListFilteredView.as_view(),
         name='route_filtered_list'),
    path("areastopslist1/<int:area_id>",
         AreaStopsListView.as_view(), name='sopts_of_area'),
    path("areastopslist", AreaStopsListView.as_view(),
         name='area_stops_filtered_list'),
]
