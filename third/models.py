from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    password = models.CharField(max_length=20, default=None, null=True)
    image = models.CharField(max_length=500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # Restaurant 모델의 Primary Key (Many-one Relation)
    # on_delete=models.CASCADE : 해당 식당 정보 삭제됐을 때 'CASCADE'가 (같이 삭제)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)