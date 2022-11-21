from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


from fares.models import Leg_Rule, Rider_Category, Transfer_Rule
from fares.tables import *
from fares.filters import LegRuleFilter


def index(request):
    return HttpResponse("Hello, world. You're at the fares index.")

def rider(request, rider_id):
    rider = Rider_Category.objects.get(pk=rider_id)
    leg_rules = Leg_Rule.objects.filter(rider_category = rider)
    # total = a.aggregate(Sum('account_value'))
    # pensions = Account.objects.filter(account_type = "pension") 
    #a = Account.objects.filter(person__name = "david").exclude(account_type = "pension") | Account.objects.filter(person__name = "henri").exclude(account_type = "pension")
    # accounts_by_type = a.values('account_type').annotate(total_value=Sum('account_value'))
    # stock_currencies = Stock.objects.filter(stock_type = "curr")
    return render(request, 'fares/rider.html', {
    'rider': rider, 'leg_rules':leg_rules, 
    }, )

class LegRuleListView(SingleTableView):
    model = Leg_Rule
    template_name = 'fares/legrulelist.html'
    table_class = LegRuleTable

    #  def get_queryset(self):
    #     queryset = super(PostListView, self).get_queryset()
    #     return queryset.filter(author.username=self.request.user.username)


class TransferListView(SingleTableView):
    model = Transfer_Rule
    template_name = 'fares/transferlist.html'
    table_class = TransferTable

class LegRuleListFilteredView(SingleTableMixin, FilterView):
    model = Leg_Rule
    table_class = LegRuleTable
    filterset_class = LegRuleFilter
    template_name = 'fares/legrulefilteredlist.html'
    
class RiderListView(SingleTableView):
    model = Rider_Category
    template_name = 'fares/riderlist.html'
    table_class = RiderTable

class NetworkListView(SingleTableView):
    model = Network
    template_name = 'fares/networklist.html'
    table_class = NetworkTable

class ProductListView(SingleTableView):
    model = Product
    template_name = 'fares/productlist.html'
    table_class = ProductTable

class AreaListView(SingleTableView):
    model = Area
    template_name = 'fares/arealist.html'
    table_class = AreaTable

class FareContainerListView(SingleTableView):
    model = Fare_Container
    template_name = 'fares/farecontainerlist.html'
    table_class = FareContainerTable