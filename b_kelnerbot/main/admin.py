from django.contrib import admin
from django import forms
from .models import MenuList, MenuElements, TableNodes, CustomerOrders, RestaurantInfo, UserReviews, KelnerBots, KelnerOrders

class MenuListAdminForm(forms.ModelForm):

    class Meta:
        model = MenuList
        fields = '__all__'


class MenuListAdmin(admin.ModelAdmin):
    form = MenuListAdminForm
    list_display = ['name', 'slug', 'menu_image', 'menu_pid']
    readonly_fields = ['name', 'slug', 'menu_image', 'menu_pid']

admin.site.register(MenuList, MenuListAdmin)


class MenuElementsAdminForm(forms.ModelForm):

    class Meta:
        model = MenuElements
        fields = '__all__'


class MenuElementsAdmin(admin.ModelAdmin):
    form = MenuElementsAdminForm
    list_display = ['dish_name', 'dish_image', 'dish_ingredients', 'dish_price', 'dish_quantity', 'dish_measure']
    # readonly_fields = ['dish_name', 'dish_image', 'dish_ingredients', 'dish_price', 'dish_quantity', 'dish_measure']

admin.site.register(MenuElements, MenuElementsAdmin)


class TableNodesAdminForm(forms.ModelForm):

    class Meta:
        model = TableNodes
        fields = '__all__'


class TableNodesAdmin(admin.ModelAdmin):
    form = TableNodesAdminForm
    list_display = ['table_id', 'table_uuid', 'is_occupied']
    readonly_fields = ['table_id', 'table_uuid', 'is_occupied']

admin.site.register(TableNodes, TableNodesAdmin)


class CustomerOrdersAdminForm(forms.ModelForm):

    class Meta:
        model = CustomerOrders
        fields = '__all__'


class CustomerOrdersAdmin(admin.ModelAdmin):
    form = CustomerOrdersAdminForm
    list_display = ['order_uuid', 'ordered_at', 'cancelled_order', 'finished_order', 'status', 'chef_name']
    readonly_fields = ['order_uuid', 'ordered_at', 'cancelled_order', 'finished_order', 'status', 'chef_name']

admin.site.register(CustomerOrders, CustomerOrdersAdmin)


class RestaurantInfoAdminForm(forms.ModelForm):

    class Meta:
        model = RestaurantInfo
        fields = '__all__'


class RestaurantInfoAdmin(admin.ModelAdmin):
    form = RestaurantInfoAdminForm
    list_display = ['name', 'last_updated', 'type', 'website', 'email', 'telephone', 'long_lat', 'restaurant_image', 'rating', 'open_date', 'close_date']
    readonly_fields = ['name', 'last_updated', 'type', 'website', 'email', 'telephone', 'long_lat', 'restaurant_image', 'rating', 'open_date', 'close_date']

admin.site.register(RestaurantInfo, RestaurantInfoAdmin)


class UserReviewsAdminForm(forms.ModelForm):

    class Meta:
        model = UserReviews
        fields = '__all__'


class UserReviewsAdmin(admin.ModelAdmin):
    form = UserReviewsAdminForm
    list_display = ['user_name', 'nationality', 'reviewed_at', 'star', 'review_desc', 'most_liked_dish', 'disliked_dish']
    readonly_fields = ['user_name', 'nationality', 'reviewed_at', 'star', 'review_desc', 'most_liked_dish', 'disliked_dish']

admin.site.register(UserReviews, UserReviewsAdmin)


class KelnerBotsAdminForm(forms.ModelForm):

    class Meta:
        model = KelnerBots
        fields = '__all__'


class KelnerBotsAdmin(admin.ModelAdmin):
    form = KelnerBotsAdminForm
    list_display = ['name', 'bot_uuid', 'bot_model', 'image']
    readonly_fields = ['name', 'bot_uuid', 'bot_model', 'image']

admin.site.register(KelnerBots, KelnerBotsAdmin)


class KelnerOrdersAdminForm(forms.ModelForm):

    class Meta:
        model = KelnerOrders
        fields = '__all__'


class KelnerOrdersAdmin(admin.ModelAdmin):
    form = KelnerOrdersAdminForm
    list_display = ['order_started', 'order_finished']
    readonly_fields = ['order_started', 'order_finished']

admin.site.register(KelnerOrders, KelnerOrdersAdmin)
