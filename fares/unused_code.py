# class LegRuleResource(resources.ModelResource):
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