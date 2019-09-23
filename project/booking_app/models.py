from django.db import models
from datetime import datetime

class Contact(models.Model):
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=75)
    your_phone = models.CharField(max_length=255)
    your_message = models.TextField()



class Tour(models.Model):
	tour_main_image = models.ImageField(null=True, upload_to='package_images/')
	tour_name = models.CharField(max_length=255) 
	tour_price = models.DecimalField(max_digits=6, decimal_places=2)
	tour_duration = models.CharField(max_length=255)
	tour_second_image = models.ImageField(null=True, upload_to='package_images/')
	tour_description = models.TextField(max_length=256, blank=True, null=True, default=None)
	day1_head = models.TextField(max_length=50, blank=True, null=True, default=None)
	day1_description = models.TextField(max_length=256, blank=True, null=True, default=None)
	day2_head = models.TextField(max_length=50, blank=True, null=True, default=None)
	day2_description = models.TextField(max_length=256, blank=True, null=True, default=None)
	day3_head = models.TextField(max_length=50, blank=True, null=True, default=None)
	day3_description = models.TextField(max_length=256, blank=True, null=True, default=None)
	day4_head = models.TextField(max_length=50, blank=True, null=True, default=None)
	day4_description = models.TextField(max_length=256, blank=True, null=True, default=None)
	day5_head = models.TextField(max_length=50, blank=True, null=True, default=None)
	day5_description = models.TextField(max_length=256, blank=True, null=True, default=None)


class Post_list(models.Model):
	post_list_image = models.ImageField(null=True, upload_to='package_images/')
	post_name = models.TextField(max_length=64, blank=True, null=True, default=None)
	post_description = models.TextField(max_length=256, blank=True, null=True, default=None)
	created_date = models.DateTimeField(default=datetime.now, blank=True)
	post_detail_name = models.TextField(max_length=64, blank=True, null=True, default=None)
	post_detail_description = models.TextField(max_length=1024, blank=True, null=True, default=None)




