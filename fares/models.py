from django.db import models

class Product(models.Model):
    ref_id = models.CharField(max_length=128, )
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=3)
    def __str__(self):
        return self.name

class Stop_Area(models.Model):
    area_id = models.ForeignKey('Area', on_delete=models.CASCADE, )
    stop_id = models.ForeignKey('Stop', on_delete=models.CASCADE, related_name='areas',)
    
    def __str__(self):
        return self.area_id.area_id + ':' + self.stop_id.stop_id

class Leg_Rule(models.Model):
    network = models.ForeignKey('Network', on_delete=models.CASCADE, )
    from_area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='area_to',null=True, blank=True)
    to_area = models.ForeignKey('Area', on_delete=models.CASCADE,  related_name='area_from',null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='leg_rules',null=True, blank=True)
    leg_group = models.ForeignKey('Leg_Group', on_delete=models.CASCADE, null=True, blank=True )
    rider_category = models.ForeignKey('Rider_Category', on_delete=models.CASCADE, null=True, blank=True)
    fare_container = models.ForeignKey('Fare_Container', on_delete=models.CASCADE,null=True, blank=True )

class Stop(models.Model):
    # stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,wheelchair_boarding,location_type,parent_station
    stop_id = models.CharField(max_length=128, )
    stop_name = models.CharField(max_length=128)
    parent_station = models.ForeignKey('Stop', on_delete=models.CASCADE,null=True, blank=True)
    
    class LocationType(models.TextChoices):
        STOP = '0', 'Stop'
        STATION = '1', 'Station'
        ENTRANCE = '2', 'Entrance or Exit'
        GENERIC = '3', 'Generic Node'
        BOARDINGPOINT = '4', 'Boarding Point'
    location_type = models.CharField(
        max_length=1,
        choices=LocationType.choices,
        default=LocationType.STOP,
    )
    
    def __str__(self):
        return self.stop_id

class Route(models.Model):
    route_id = models.CharField(max_length=128, )
    route_short_name = models.CharField(max_length=128,blank=True , null=True)
    route_long_name = models.CharField(max_length=128,blank=True , null=True)
    network_id  = models.ForeignKey('Network', on_delete=models.CASCADE, blank=True , null=True)

    class AsRouteType(models.TextChoices):
        NO = '0', 'No'
        YES = '1', 'Yes'
        
    as_route = models.CharField(
        max_length=1,
        choices=AsRouteType.choices,
        default=None,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.route_short_name

class Leg_Group(models.Model):
    ref_id =  models.CharField(max_length=128, blank=False, default="set me")
    def __str__(self):
        return self.ref_id

class Transfer_Rule(models.Model):
    from_leg_group = models.ForeignKey('Leg_Group', on_delete=models.CASCADE,related_name='transfer_from' )
    to_leg_group = models.ForeignKey('Leg_Group', on_delete=models.CASCADE, related_name='transfer_to')
    fare_product = models.ForeignKey('Product', on_delete=models.CASCADE, )
    transfer_count = models.IntegerField(null=True, blank=True)
    duration_limit = models.PositiveIntegerField(null=True, blank=True)
    
    class DurationLimitType(models.TextChoices):
        DEPTOARR = '0', '1st leg departure to 2nd leg arrival'
        DEPTODEP = '1', '1st leg departure to 2nd leg departure'
        ARRTODEP = '2', '1st leg arrival to 2nd leg departure'
        ARRTOARR = '3', '1st leg arrival to 2nd leg arrival'
    
    duration_limit_type = models.CharField(
        max_length=1,
        choices=DurationLimitType.choices,
        default=DurationLimitType.DEPTOARR,
    )

    class FareTransferType(models.TextChoices):
        A_AB = '0', 'From leg + transfer price'
        A_AB_B = '1', 'From leg + transfer + to leg price'
        AB = '2', 'transfer price only'
    
    fare_transfer_type = models.CharField(
        max_length=6,
        choices=FareTransferType.choices,
        default=FareTransferType.A_AB,
    )
    
    notes = models.CharField(max_length=256, null=True, blank=True)

class Rider_Category(models.Model):
    ref_id =  models.CharField(max_length=128, blank=False, )
    name = models.CharField(max_length=128)
    min_age = models.PositiveIntegerField(null=True, blank=True)
    max_age = models.PositiveIntegerField(null=True, blank=True)
    eligibility_url = models.URLField(null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.ref_id

class Fare_Container(models.Model):
    ref_id =  models.CharField(max_length=128, blank=False, )
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    rider_category = models.ForeignKey('Rider_Category', on_delete=models.CASCADE, null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)
    def __str__(self):
        return self.ref_id

class Network(models.Model):
    ref_id =  models.CharField(max_length=128, blank=False, )
    def __str__(self):
        return self.ref_id

class Area(models.Model):
    area_id =  models.CharField(max_length=128, blank=False, )
    
    def __str__(self):
        return self.area_id