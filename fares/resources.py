from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from fares.models import *

class LegRuleResource(resources.ModelResource):

    network_id = Field(
        attribute='network',
        column_name='network_id',
        widget=ForeignKeyWidget(Network, 'ref_id'))

    from_area_id = Field(
        attribute='from_area',
        column_name='from_area_id',
        widget=ForeignKeyWidget(Area, 'area_id'))

    to_area_id = Field(
        attribute='to_area',
        column_name='to_area_id',
        widget=ForeignKeyWidget(Area, 'area_id'))

    fare_product_id = Field(
        attribute='product',
        column_name='fare_product_id',
        widget=ForeignKeyWidget(Product, 'ref_id'))

    leg_group_id = Field(
        attribute='leg_group',
        column_name='leg_group_id',
        widget=ForeignKeyWidget(Leg_Group, 'ref_id'))

    rider_category_id = Field(
        attribute='rider_category',
        column_name='rider_category_id',
        widget=ForeignKeyWidget(Rider_Category,'ref_id'))

    fare_container_id = Field(
        attribute='fare_container',
        column_name='fare_container_id',
        widget=ForeignKeyWidget(Fare_Container, 'ref_id'))

    # print (fare_container_id)
    def before_import_row(self, row, row_number=None, **kwargs):
        # we going to create any missing leg_group_ids
        leg_group_id = row.get('leg_group_id')
        if leg_group_id != '':
            Leg_Group.objects.get_or_create(ref_id=leg_group_id)



    class Meta:
        model = Leg_Rule
        exclude = ('id', 'from_area','to_area','network','product','rider_category','leg_group','fare_container')
        import_id_fields = ('network_id','from_area_id','to_area_id','rider_category_id','fare_container_id')

class ProductResource(resources.ModelResource):
    ref_id = Field(attribute='ref_id', column_name='fare_product_id')
    name = Field(attribute='name', column_name='fare_product_name')
    class Meta:
        model = Product
        exclude = ('id', 'ref_id','name')
        import_id_fields = ('ref_id',)
    
class RiderResource(resources.ModelResource):
    ref_id = Field(attribute='ref_id', column_name='rider_category_id')
    name = Field(attribute='name', column_name='rider_category_name')
    class Meta:
        model = Rider_Category
        exclude = ('id', 'ref_id','name')
        import_id_fields = ('ref_id',)

class TransferRuleResource(resources.ModelResource):
    from_leg_group_id = Field(
        attribute='from_leg_group',
        column_name='from_leg_group_id',
        widget=ForeignKeyWidget(Leg_Group,'ref_id'))
    
    to_leg_group_id = Field(
        attribute='to_leg_group',
        column_name='to_leg_group_id',
        widget=ForeignKeyWidget(Leg_Group,'ref_id'))
    
    fare_product_id = Field(
        attribute='fare_product',
        column_name='fare_product_id',
        widget=ForeignKeyWidget(Product,'ref_id'))
    
    class Meta:
        model = Transfer_Rule
        exclude = ('id', 'ref_id','name','from_leg_group','to_leg_group','fare_product')
        import_id_fields = ('from_leg_group_id','to_leg_group_id')

class FareContainerResource(resources.ModelResource):
    fare_container_id = Field(attribute='ref_id', column_name='fare_container_id')
    name = Field(attribute='name', column_name='fare_container_name')
    rider_category = Field(
        attribute='rider_category',
        column_name='rider_category_id',
        widget=ForeignKeyWidget(Rider_Category,'ref_id'))
    
    class Meta:
        model = Fare_Container
        exclude = ('id', 'ref_id','rider_category',)
        import_id_fields = ('fare_container_id',)

class AreaResource(resources.ModelResource):
    # area_id = Field(attribute='ref_id', column_name='area_id')
    
    class Meta:
        model = Area
        exclude = ('id',)
        import_id_fields = ('area_id',)

class StopResource(resources.ModelResource):
    parent_station = Field(
        attribute='parent_station',
        column_name='parent_station',
        widget=ForeignKeyWidget(Stop,'stop_id'))

    def before_import_row(self, row, row_number=None, **kwargs):
        # we going to create any missing parent station - its attribute will be updatd by the later row
        parent_station_id = row.get('parent_station')
        if parent_station_id != '':
            Stop.objects.get_or_create(stop_id=parent_station_id)
            
    class Meta:
        model = Stop
        exclude = ('id',)
        import_id_fields = ('stop_id',)
        use_bulk = True

class RouteResource(resources.ModelResource):
    network_id = Field(
        attribute='network_id',
        column_name='network_id',
        widget=ForeignKeyWidget(Network, 'ref_id'))
    
    def before_import_row(self, row, row_number=None, **kwargs):
        # we going to create any missing network
        network_id = row.get('network_id')
        if network_id != '':
            Network.objects.get_or_create(ref_id=network_id)

    class Meta:
        model = Route
        exclude = ('id',)
        import_id_fields = ('route_id',)

class StopAreaResource(resources.ModelResource):
    stop_id = Field(
        attribute='stop_id',
        column_name='stop_id',
        widget=ForeignKeyWidget(Stop,'stop_id'))
    
    area_id = Field(
        attribute='area_id',
        column_name='area_id',
        widget=ForeignKeyWidget(Area,'area_id'))
    
    class Meta:
        model = Stop_Area
        exclude = ('id',)
        import_id_fields = ('stop_id','area_id',)
        use_bulk = True