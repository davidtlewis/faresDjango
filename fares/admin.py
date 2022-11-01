from django.contrib import admin

from .models import *

# class LegInLineAdmin(admin.TabularInline):
#     model = Leg_Rule

class LegRuleAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ("id", "network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_editable = ("network", "from_area","to_area", "rider_category","fare_container", "product", "leg_group")
    list_filter = ("network","rider_category","fare_container",)

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
