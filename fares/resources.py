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
        widget=ForeignKeyWidget(Area, 'ref_id'))

    to_area_id = Field(
        attribute='to_area',
        column_name='to_area_id',
        widget=ForeignKeyWidget(Area, 'ref_id'))

    fare_product_id = Field(
        attribute='product',
        column_name='product_id',
        widget=ForeignKeyWidget(Product, 'ref_id'))

    leg_group = Field(
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

    class Meta:
        model = Leg_Rule
        exclude = ('id', 'from_area','to_area','network','product','rider_category','leg_group','fare_container')
        import_id_fields = ('network_id','from_area_id','to_area_id','rider_category_id','fare_container_id')
        # import_id_fields = ('from_area','to_area','rider_category','fare_container')
    
    # def before_import_row(self, row, row_number=None, **kwargs):
    #     network_id = row.get('network_id')
    #     if network_id == None:
    #         network_id = "EMPTY"
    #     row["network_id"] = Network.objects.get(ref_id=network_id)
    #     print( row["network_id"])
        
    #     from_area_id = row.get('from_area_id')
    #     if from_area_id == None:
    #         from_area_id = "EMPTY"
    #     row["from_area_id"] = Area.objects.get(ref_id=from_area_id)
    #     print( row["from_area_id"])
    #     to_area_id = row.get('to_area_id')
    #     if to_area_id == '':
    #         to_area_id = "EMPTY"
    #     row['to_area_id'] = Area.objects.get(ref_id=to_area_id)
    #     print( row["to_area_id"])
        
    #     rider_category_id = row.get('rider_category_id')
    #     if rider_category_id == None:
    #         rider_category_id = "EMPTY"
    #     row['rider_category_id'] = Rider_Category.objects.get(ref_id=rider_category_id)
    #     print( row["rider_category_id"])
        
    #     fare_container_id = row.get('fare_container_id')
    #     if fare_container_id == None:
    #         fare_container_id = "EMPTY"
    #     row['fare_container_id'] = Fare_Container.objects.get(ref_id=fare_container_id)
    #     print( row["fare_container_id"])
        
    #     fare_product_id = row.get('fare_product_id')
    #     if fare_product_id == None:
    #         fare_product_id = "EMPTY"
    #     row['fare_product_id'] = Product.objects.get(ref_id=fare_product_id)
    #     print(row['fare_product_id'])
    
    #     leg_group_id = row.get('leg_group_id')
    #     if leg_group_id == None:
    #         leg_group_id = "EMPTY"
    #     row['leg_group_id'] = Leg_Group.objects.get(ref_id=leg_group_id)
    #     print(row['leg_group_id'])

    # def before_import_row(self, row, row_number=None, **kwargs):
    #     network_id = row.get('network_id')
    #     if network_id == '':
    #         network_id = "EMPTY"
    #     row["network_id"] = network_id
    #     print( row["network_id"])
        
    #     from_area_id = row.get('from_area_id')
    #     if from_area_id == '':
    #         from_area_id = "EMPTY"
    #     row["from_area_id"] = from_area_id
    #     print( row["from_area_id"])
        
    #     to_area_id = row.get('to_area_id')
    #     if to_area_id == '':
    #         to_area_id = "EMPTY"
    #     row['to_area_id'] = to_area_id
    #     print( row["to_area_id"])
        
    #     rider_category_id = row.get('rider_category_id')
    #     if rider_category_id == '':
    #         rider_category_id = "EMPTY"
    #     row['rider_category_id'] = rider_category_id
    #     print( row["rider_category_id"])
        
    #     fare_container_id = row.get('fare_container_id')
    #     if fare_container_id == '':
    #         fare_container_id = "EMPTY"
    #     row['fare_container_id'] = fare_container_id
    #     print( row["fare_container_id"])
        
    #     fare_product_id = row.get('fare_product_id')
    #     if fare_product_id == '':
    #         fare_product_id = "EMPTY"
    #     row['fare_product_id'] = fare_product_id
    #     print(row['fare_product_id'])
    
    #     leg_group_id = row.get('leg_group_id')
    #     if leg_group_id == '':
    #         leg_group_id = "EMPTY"
    #     row['leg_group_id'] = ref_id=leg_group_id

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
    area_id = Field(attribute='ref_id', column_name='area_id')
    
    class Meta:
        model = Area
        exclude = ('id', 'ref_id',)

class StopResource(resources.ModelResource):
    parent_station = Field(
        attribute='parent_station',
        column_name='parent_station',
        widget=ForeignKeyWidget(Stop,'stop_id'))

    class Meta:
        model = Stop
        exclude = ('id',)
        import_id_fields = ('stop_id',)

class RouteResource(resources.ModelResource):
    network_id = Field(
        attribute='network_id',
        column_name='network_id',
        widget=ForeignKeyWidget(Network, 'ref_id'))
    
    # def before_import_row(self, row, row_number=None, **kwargs):
    #     network_id = row.get('network_id')
    #     if network_id == None:
    #         network_id = "EMPTY"
    #     row["network_id"] = Network.objects.get(ref_id=network_id)

    class Meta:
        model = Route
        exclude = ('id',)
        import_id_fields = ('route_id',)