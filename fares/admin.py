from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from fares.resources import *


from .models import *

# class LegInLineAdmin(admin.TabularInline):
#     model = Leg_Rule


class LegRuleAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id", "network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_editable = ("network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_filter = ("network","rider_category","fare_container",)
    resource_classes = [LegRuleResource]

class ProductAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id", "ref_id", "name", "amount", "currency","associated_rules_count")
    list_editable = ("ref_id", "name", "amount", "currency",)
    resource_classes = [ProductResource]
    # inlines = [LegInLineAdmin]

    def associated_rules_count(elf, obj):
        return obj.leg_rules.all().count()

class RiderAdmin(ImportExportModelAdmin):
    list_display = ("id", "ref_id", "name", "min_age", "max_age", "eligibility_url","notes",)
    list_editable = ("ref_id", "name", "min_age", "max_age", "eligibility_url","notes",)
    resource_classes = [RiderResource,]

class TransferRuleAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id","from_leg_group", "to_leg_group", "fare_product", "transfer_count","duration_limit", "duration_limit_type","fare_transfer_type")
    list_editable = ("from_leg_group", "to_leg_group", "fare_product", "transfer_count","duration_limit", "duration_limit_type","fare_transfer_type")
    resource_classes = [TransferRuleResource,]

class FareContainerAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id", "ref_id", "name", "amount","currency", "rider_category",)
    list_editable = ("ref_id", "name", "amount","currency", "rider_category",)
    resource_classes = [FareContainerResource]

class LegGroupAdmin(admin.ModelAdmin):
    # TODO need to deal wih the fact leg groups  does not exist as a file - it is derived from fare_leg_rules.txt
    save_as = True
    list_display = ("id", "ref_id",)
    list_editable = ("ref_id", ) 

class NetworkAdmin(admin.ModelAdmin):
    # TODO need to deal wih the fact netowrks does not exost as a file - it is derived from stop_areas.txt
    # list_display = ("id", "ref_id",)
    # list_editable = ("ref_id", ) 
    pass

class AreaAdmin(ImportExportModelAdmin):
    list_display = ("id", "ref_id",)
    list_editable = ("ref_id", ) 
    resource_classes = [AreaResource]

class StopAdmin(ImportExportModelAdmin):
    list_display = ("stop_id", "stop_name","parent_station","location_type")
    # list_editable = ("ref_id", ) 
    resource_classes = [StopResource]

class AreaAdmin(ImportExportModelAdmin):
    list_display = ("area_id", )
    # list_editable = ("area_id", ) 

class RouteAdmin(ImportExportModelAdmin):
    list_display = ("route_id", "route_short_name","route_long_name","network_id","as_route")
    # list_editable = ("ref_id", ) 
    resource_classes = [RouteResource]

class StopAreaAdmin(ImportExportModelAdmin):
    list_display = ("stop_id", "area_id",)
    # list_editable = ("ref_id", ) 
    resource_classes = [StopAreaResource]



admin.site.register(Product, ProductAdmin)
admin.site.register(Leg_Rule, LegRuleAdmin)
admin.site.register(Leg_Group, LegGroupAdmin)
admin.site.register(Transfer_Rule, TransferRuleAdmin)
admin.site.register(Rider_Category, RiderAdmin)
admin.site.register(Fare_Container, FareContainerAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Stop, StopAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Stop_Area, StopAreaAdmin)
