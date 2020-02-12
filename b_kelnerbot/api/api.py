from main import models
from . import serializers
from rest_framework import viewsets, permissions


class MenuListViewSet(viewsets.ModelViewSet):
    """ViewSet for the MenuList class"""

    queryset = models.MenuList.objects.all()
    serializer_class = serializers.MenuListSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MenuElementsViewSet(viewsets.ModelViewSet):
    """ViewSet for the MenuElements class"""

    queryset = models.MenuElements.objects.all()
    serializer_class = serializers.MenuElementsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TableNodesViewSet(viewsets.ModelViewSet):
    """ViewSet for the TableNodes class"""

    queryset = models.TableNodes.objects.all()
    serializer_class = serializers.TableNodesSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CustomerOrdersViewSet(viewsets.ModelViewSet):
    """ViewSet for the CustomerOrders class"""

    queryset = models.CustomerOrders.objects.all()
    serializer_class = serializers.CustomerOrdersSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RestaurantInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the RestaurantInfo class"""

    queryset = models.RestaurantInfo.objects.all()
    serializer_class = serializers.RestaurantInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserReviewsViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserReviews class"""

    queryset = models.UserReviews.objects.all()
    serializer_class = serializers.UserReviewsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class KelnerBotsViewSet(viewsets.ModelViewSet):
    """ViewSet for the KelnerBots class"""

    queryset = models.KelnerBots.objects.all()
    serializer_class = serializers.KelnerBotsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class KelnerOrdersViewSet(viewsets.ModelViewSet):
    """ViewSet for the KelnerOrders class"""

    queryset = models.KelnerOrders.objects.all()
    serializer_class = serializers.KelnerOrdersSerializer
    # permission_classes = [permissions.IsAuthenticated]
