from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import csv
from django.http import HttpResponseRedirect
from django.urls import reverse



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

def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "fares/upload.html", data)
    # if not GET, then proceed
    csv_file = request.FILES["csv_file"]
    
    #if file is too large, return
    if csv_file.multiple_chunks():
        messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        return HttpResponseRedirect(reverse("upload"))

    decoded_file = csv_file.read().decode('utf-8').splitlines()
    file_data = csv.DictReader(decoded_file, )

    for row in file_data:
        # create a fare_lef_rule for each row - as long as all referenced objects exists
        print(row)
        network = Network.objects.filter(ref_id=row['network_id']).first()
        from_area = Area.objects.filter(ref_id=row['from_area_id']).first()
        to_area = Area.objects.filter(ref_id=row['to_area_id']).first()
        product = Product.objects.filter(ref_id=row['fare_product_id']).first()
        leg_group = Leg_Group.objects.filter(ref_id=row['leg_group_id']).first()
        rider_category = Rider_Category.objects.filter(ref_id=row['rider_category_id']).first()
        fare_container = Fare_Container.objects.filter(ref_id=row['fare_container_id']).first()
        # TODO check if there was a key that it matched!
        # validation = True
        # if network is None:
        #     validation = False
        #     errorMessage = f"Row: number network: {row['network']} not found./n"
        lg = Leg_Rule(
            network=network,
            from_area=from_area, 
            to_area=to_area, 
            product=product,
            leg_group=leg_group,
            rider_category=rider_category,
            fare_container=fare_container,
        )
        lg.save()
        print(lg)

    
    return HttpResponseRedirect(reverse("upload"))