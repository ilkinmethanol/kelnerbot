from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import CommaSeparatedIntegerField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import FloatField
from django.db.models import ImageField
from django.db.models import IntegerField
from django.db.models import TextField
from django.db.models import URLField
from django.db.models import UUIDField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.core.validators import validate_comma_separated_integer_list
import uuid
class MenuList(models.Model):

    # Fields
    name = models.CharField(max_length=20)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    menu_image = models.ImageField(upload_to="media/menu_images/")
    menu_pid = models.UUIDField(default=uuid.uuid4, editable=False)
    products = models.ManyToManyField('MenuElements',related_name="menu_elements")

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('main_menulist_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('main_menulist_update', args=(self.slug,))


class MenuElements(models.Model):

    # Fields
    dish_name = models.CharField(max_length=30)
    dish_image = models.ImageField(upload_to="media/dish/")
    dish_ingredients = models.TextField(max_length=200)
    dish_price = models.FloatField()
    dish_quantity = models.IntegerField()
    dish_measure = models.CharField(max_length=5)

    # Relationship Fields
    dish_type = models.ForeignKey(
        'main.MenuList',
        on_delete=models.CASCADE, related_name="dish_type_menulist"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('main_menuelements_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('main_menuelements_update', args=(self.pk,))


class TableNodes(models.Model):

    # Fields
    table_id = models.IntegerField()
    table_uuid = models.UUIDField()
    is_occupied = models.BooleanField(default="False")


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('main_tablenodes_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('main_tablenodes_update', args=(self.pk,))


class CustomerOrders(models.Model):

    # Fields
    order_uuid = models.UUIDField()
    ordered_at = models.DateTimeField()
    cancelled_order = models.BooleanField(default=0)
    finished_order = models.BooleanField()
    status = models.IntegerField()
    chef_name = models.CharField(max_length=10)

    # Relationship Fields
    ordered_by = models.ForeignKey(
        'main.TableNodes',
        on_delete=models.CASCADE, related_name="ordered_by_tablenodes"
    )
    dish_list = models.ForeignKey(
        'main.MenuElements',
        on_delete=models.CASCADE, related_name="dish_list_menuelements"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('main_customerorders_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('main_customerorders_update', args=(self.pk,))


class RestaurantInfo(models.Model):

    # Fields
    name = models.CharField(max_length=20)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=30)
    website = models.URLField()
    email = models.EmailField()
    telephone = models.CharField(max_length=25)
    long_lat = models.CharField(validators=[validate_comma_separated_integer_list], max_length=22)
    restaurant_image = models.ImageField(upload_to="media/restaurant/")
    rating = models.IntegerField()
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()

    # Relationship Fields
    menu_list = models.ForeignKey(
        'main.MenuList',
        on_delete=models.CASCADE, related_name="menu_list_menulist"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('main_restaurantinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('main_restaurantinfo_update', args=(self.pk,))


class UserReviews(models.Model):

    # Fields
    user_name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    reviewed_at = models.DateTimeField()
    star = models.IntegerField()
    review_desc = models.TextField(max_length=100)
    most_liked_dish = models.CharField(max_length=20)
    disliked_dish = models.CharField(max_length=25)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('main_userreviews_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('main_userreviews_update', args=(self.pk,))


class KelnerBots(models.Model):

    # Fields
    name = models.CharField(max_length=20)
    bot_uuid = models.UUIDField()
    bot_model = models.CharField(max_length=10)
    image = models.ImageField(upload_to="media/kelners/")


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('main_kelnerbots_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('main_kelnerbots_update', args=(self.pk,))


class KelnerOrders(models.Model):

    # Fields
    order_started = models.DateTimeField()
    order_finished = models.DateTimeField()

    # Relationship Fields
    kelner = models.ForeignKey(
        'main.KelnerBots',
        on_delete=models.CASCADE, related_name="kelners"
    )
    order = models.ForeignKey(
        'main.CustomerOrders',
        on_delete=models.CASCADE, related_name="orders"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('main_kelnerorders_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('main_kelnerorders_update', args=(self.pk,))


# class Events(models.Model):

#     #Fields
#     event_name = models.CharField(max_length=20)
#     event_date_from = models.DateTimeField()
#     event_date_to = models.DateTimeField()
#     event_type = models.CharField(max_length=10)
#     event_description = models.TextField()
#     event_price = models.CharField(max_length=10)

#     class Meta:
#         ordering = ('-pk')

#     def __unicode__(self):
#         return u'%s' % self.event_name
