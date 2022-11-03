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
    # Think anout using natural keys !
    # https://docs.djangoproject.com/en/4.1/topics/serialization/#:~:text=A%20natural%20key%20is%20a,using%20the%20primary%20key%20value.

class LegRuleAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ("id", "network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_editable = ("network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_filter = ("network","rider_category","fare_container",)
    resource_classes = [LegRuleResource]

class ProductAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ("id", "ref_id", "name", "amount", "currency","associated_rules_count")
    list_editable = ("ref_id", "name", "amount", "currency",)
    
    # inlines = [LegInLineAdmin]

    def associated_rules_count(elf, obj):
        return obj.leg_rules.all().count()


class RiderAdmin(admin.ModelAdmin):
    list_display = ("id", "ref_id", "name", "min_age", "max_age", "eligibility_url","notes",)
    list_editable = ("ref_id", "name", "min_age", "max_age", "eligibility_url","notes",)

class TransferAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ("id","from_leg_group", "to_leg_group", "fare_product", "transfer_count","duration_limit", "duration_limit_type","fare_transfer_type")
    list_editable = ("from_leg_group", "to_leg_group", "fare_product", "transfer_count","duration_limit", "duration_limit_type","fare_transfer_type")

class ContainerAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ("id", "ref_id", "name", "amount","currency", "rider_category",)
    list_editable = ("ref_id", "name", "amount","currency", "rider_category",)

class LegGroupAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ("id", "ref_id",)
    list_editable = ("ref_id", ) 

class NetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "ref_id",)
    list_editable = ("ref_id", ) 

class AreaAdmin(admin.ModelAdmin):
    list_display = ("id", "ref_id",)
    list_editable = ("ref_id", ) 

admin.site.register(Product, ProductAdmin)
admin.site.register(Leg_Rule, LegRuleAdmin)
admin.site.register(Leg_Group, LegGroupAdmin)
admin.site.register(Transfer_Rule, TransferAdmin)
admin.site.register(Rider_Category, RiderAdmin)
admin.site.register(Fare_Container, ContainerAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Area, AreaAdmin)

