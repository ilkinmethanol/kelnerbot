from main import models
from rest_framework import serializers


class MenuListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MenuList
        fields = (
            'slug',
            'name',
            'menu_image',
            'menu_pid',
            'products'
        )
        depth = 2


class MenuElementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MenuElements
        fields = (
            'pk',
            'dish_name',
            'dish_image',
            'dish_ingredients',
            'dish_price',
            'dish_quantity',
            'dish_measure',
        )


class TableNodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TableNodes
        fields = (
            'pk',
            'table_id',
            'table_uuid',
            'is_occupied',
        )


class CustomerOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerOrders
        fields = (
            'pk',
            'order_uuid',
            'ordered_at',
            'cancelled_order',
            'finished_order',
            'status',
            'chef_name',
        )


class RestaurantInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RestaurantInfo
        fields = (
            'pk',
            'name',
            'last_updated',
            'type',
            'website',
            'email',
            'telephone',
            'long_lat',
            'restaurant_image',
            'rating',
            'open_date',
            'close_date',
        )


class UserReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserReviews
        fields = (
            'pk',
            'user_name',
            'nationality',
            'reviewed_at',
            'star',
            'review_desc',
            'most_liked_dish',
            'disliked_dish',
        )


class KelnerBotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KelnerBots
        fields = (
            'pk',
            'name',
            'bot_uuid',
            'bot_model',
            'image',
        )


class KelnerOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KelnerOrders
        fields = (
            'pk',
            'order_started',
            'order_finished',
        )


class CustomerOrderSerializer(serializers.Serializer):
    table_num = serializers.CharField(max_length=5)
    ordered_at = serializers.DateTimeField()
    final_amount = serializers.FloatField()
    orders = serializers.JSONField()
    