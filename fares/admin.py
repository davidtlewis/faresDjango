from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin

from .models import *

# class LegInLineAdmin(admin.TabularInline):
#     model = Leg_Rule

class LegRuleResource(resources.ModelResource):
    network = Field(attribute='network__ref_id', column_name='network')
    from_area = Field(attribute='from_area__ref_id', column_name='from_area')
    to_area = Field(attribute='to_area__ref_id', column_name='to_area')
    product = Field(attribute='product__ref_id', column_name='product')
    leg_group = Field(attribute='leg_group__ref_id', column_name='leg_group')
    rider_category = Field(attribute='rider_category__ref_id', column_name='rider_category')
    fare_container = Field(attribute='fare_container__ref_id', column_name='fare_container')
    class Meta:
        model = Leg_Rule
        exclude = ('id', )

class LegRuleAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id", "network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_editable = ("network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_filter = ("network","rider_category","fare_container",)
    resource_classes = [LegRuleResource]

class ProductResource(resources.ModelResource):
    fare_product_id = Field(attribute='ref_id', column_name='fare_product_id')
    fare_product_name = Field(attribute='name', column_name='fare_product_name')
    class Meta:
        model = Product
        exclude = ('id', 'ref_id','name')

class ProductAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id", "ref_id", "name", "amount", "currency","associated_rules_count")
    list_editable = ("ref_id", "name", "amount", "currency",)
    resource_classes = [ProductResource]
    # inlines = [LegInLineAdmin]

    def associated_rules_count(elf, obj):
        return obj.leg_rules.all().count()


class RiderResource(resources.ModelResource):
    rider_category_id = Field(attribute='ref_id', column_name='rider_category_id')
    rider_category_name = Field(attribute='name', column_name='rider_category_name')
    class Meta:
        model = Rider_Category
        exclude = ('id', 'ref_id','name')

class RiderAdmin(ImportExportModelAdmin):
    list_display = ("id", "ref_id", "name", "min_age", "max_age", "eligibility_url","notes",)
    list_editable = ("ref_id", "name", "min_age", "max_age", "eligibility_url","notes",)
    resource_classes = [RiderResource,]

class TransferRuleResource(resources.ModelResource):
    from_leg_group_id = Field(attribute='from_leg_group__ref_id', column_name='from_leg_group_id')
    to_leg_group_id = Field(attribute='to_leg_group__ref_id', column_name='to_leg_group_id')
    fare_product_id = Field(attribute='fare_product__ref_id', column_name='fare_product_id')
    class Meta:
        model = Transfer_Rule
        exclude = ('id', 'ref_id','name','from_leg_group','to_leg_group','fare_product')

class TransferRuleAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id","from_leg_group", "to_leg_group", "fare_product", "transfer_count","duration_limit", "duration_limit_type","fare_transfer_type")
    list_editable = ("from_leg_group", "to_leg_group", "fare_product", "transfer_count","duration_limit", "duration_limit_type","fare_transfer_type")
    resource_classes = [TransferRuleResource,]

class FareContainerResource(resources.ModelResource):
    fare_container_id = Field(attribute='ref_id', column_name='fare_container_id')
    fare_container_name = Field(attribute='name', column_name='fare_container_name')
    rider_category_id = Field(attribute='rider_category__ref_id', column_name='rider_category_id')
    class Meta:
        model = Fare_Container
        exclude = ('id', 'ref_id','name','rider_category')





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
    list_display = ("id", "ref_id",)
    list_editable = ("ref_id", ) 

class AreaResource(resources.ModelResource):
    area_id = Field(attribute='ref_id', column_name='area_id')
    
    class Meta:
        model = Area
        exclude = ('id', 'ref_id',)

class AreaAdmin(ImportExportModelAdmin):
    list_display = ("id", "ref_id",)
    list_editable = ("ref_id", ) 
    resource_classes = [AreaResource]

admin.site.register(Product, ProductAdmin)
admin.site.register(Leg_Rule, LegRuleAdmin)
admin.site.register(Leg_Group, LegGroupAdmin)
admin.site.register(Transfer_Rule, TransferRuleAdmin)
admin.site.register(Rider_Category, RiderAdmin)
admin.site.register(Fare_Container, FareContainerAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Area, AreaAdmin)

