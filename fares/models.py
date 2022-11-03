from django.db import models
# from django.conf import settings
# we are branching this

class Product(models.Model):
    ref_id = models.CharField(max_length=128, )
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=3)
    def __str__(self):
        return self.name

class Leg_Rule(models.Model):
    network = models.ForeignKey('Network', on_delete=models.CASCADE, )
    from_area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='area_to',null=True, blank=True)
    to_area = models.ForeignKey('Area', on_delete=models.CASCADE,  related_name='area_from',null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='leg_rules')
    leg_group = models.ForeignKey('Leg_Group', on_delete=models.CASCADE, null=True, blank=True )
    rider_category = models.ForeignKey('Rider_Category', on_delete=models.CASCADE, null=True, blank=True)
    fare_container = models.ForeignKey('Fare_Container', on_delete=models.CASCADE,null=True, blank=True )

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
    ref_id =  models.CharField(max_length=128, blank=False, )
    
    def __str__(self):
        return self.ref_id