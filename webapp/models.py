# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    tg_id = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class AllUsers(models.Model):
    u_id = models.AutoField(primary_key=True)
    tg_u_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'all_users'


class Cart(models.Model):
    carts_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AllUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart'


class CartProducts(models.Model):
    cart_id = models.IntegerField()
    dish = models.ForeignKey('Dish', models.DO_NOTHING)
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart_products'


class Clients(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(AllUsers, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Dish(models.Model):
    d_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=500)
    dish_desc = models.CharField(max_length=1000, blank=True, null=True)
    dish_photo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dish'


class Liked(models.Model):
    user = models.ForeignKey(AllUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'liked'


class LikedProduct(models.Model):
    liked = models.ForeignKey(Liked, models.DO_NOTHING)
    dish = models.ForeignKey(Dish, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'liked_product'


class Menu(models.Model):
    m_id = models.AutoField(primary_key=True)
    dish = models.ForeignKey(Dish, models.DO_NOTHING)
    price = models.IntegerField(blank=True, null=True)
    sale = models.ForeignKey('Sales', models.DO_NOTHING, db_column='sale', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class OrderDishes(models.Model):
    dish = models.ForeignKey(Dish, models.DO_NOTHING)
    ord = models.ForeignKey('Orders', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_dishes'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'


class Requests(models.Model):
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    type_req = models.CharField(max_length=200, blank=True, null=True)
    req_desc = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'


class Sales(models.Model):
    s_id = models.AutoField(primary_key=True)
    dish = models.ForeignKey(Dish, models.DO_NOTHING)
    sale = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'
