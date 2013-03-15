from django.db import models

class Plant(models.Model):
    common_name = models.CharField(max_length=50)
    genus = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    zone = models.IntegerField()
    featureColor = models.CharField(max_length=20)
    nativeRegion = models.CharField(max_length=50)
#     plant_image = models.ImageField(upload_to="images/", blank="True")
    thingy = models.CharField(max_length=50, blank="True")
    plantDescription = models.TextField()    
# should below be an organized list? see model field reference in docs. bush tree vine etc
    plantType = models.CharField(max_length=20)
# blooming time choice set   
    SPRING = 'Spring'
    SUMMER = 'Summer'
    FALL = 'Fall'
    WINTER = 'Winter'
    BLOOM_TIME_CHOICES = (
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
    )
    bloom_time = models.CharField(max_length=15,
        choices=BLOOM_TIME_CHOICES, 
        default=SPRING
    )
# sunlight-needs choice set    
    FULL_SUN = 'Full Sun'
    PART_SUN = 'Part Sun'
    SHADE = 'Shade'
    SUN_NEEDS_CHOICES = (
        (FULL_SUN, 'Full Sun'),
        (PART_SUN, 'Part Sun'),
        (SHADE, 'Shade'),
    )
    sun_needs = models.CharField(max_length=15,
        choices=SUN_NEEDS_CHOICES,
        default = FULL_SUN
    )
    

    def __unicode__(self):
        return self.common_name
        