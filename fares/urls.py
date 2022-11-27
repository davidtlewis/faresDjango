from django.urls import path

from . import views
from fares.views import LegRuleListView, LegRuleListFilteredView, TransferListView, RiderListView, NetworkListView, ProductListView, FareContainerListView

urlpatterns = [
    path('', views.index, name='index'),
    path('rider/<int:rider_id>', views.rider, name='rider_detail'),
    path("legrulelist", LegRuleListView.as_view(), name='legrule_list'),
    path("transferlist", TransferListView.as_view(), name='transfer_list'),
    path("legrulelistfiltered", LegRuleListFilteredView.as_view(), name='legrule_filtered_list'),
    path("transferlist", TransferListView.as_view(), name='transfer_list'),
    path("riderlist", RiderListView.as_view(), name='rider_list'),
    path("networklist", NetworkListView.as_view(), name='network_list'),
    path("productlist", ProductListView.as_view(), name='product_list'),
    path("farecontainerlist", FareContainerListView.as_view(), name='fareconatiner_list'),
    path('upload', views.upload_csv, name='upload'),
]