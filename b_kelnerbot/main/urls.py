from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from api import api
from . import views

router = routers.DefaultRouter()
router.register(r'menulist', api.MenuListViewSet)
router.register(r'menuelements', api.MenuElementsViewSet)
router.register(r'tablenodes', api.TableNodesViewSet)
router.register(r'customerorders', api.CustomerOrdersViewSet)
router.register(r'restaurantinfo', api.RestaurantInfoViewSet)
router.register(r'userreviews', api.UserReviewsViewSet)
router.register(r'kelnerbots', api.KelnerBotsViewSet)
router.register(r'kelnerorders', api.KelnerOrdersViewSet)

from api.views import helloApi

urlpatterns = [
    # urls for Django Rest Framework API
    path('a_rest/restaurant/', include(router.urls)),
    path('hello/',helloApi.as_view()),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# urlpatterns += (
#     # urls for MenuList
#     path('main/menulist/', views.MenuListListView.as_view(), name='main_menulist_list'),
#     path('main/menulist/create/', views.MenuListCreateView.as_view(), name='main_menulist_create'),
#     path('main/menulist/detail/<slug:slug>/', views.MenuListDetailView.as_view(), name='main_menulist_detail'),
#     path('main/menulist/update/<slug:slug>/', views.MenuListUpdateView.as_view(), name='main_menulist_update'),
# )
#
# urlpatterns += (
#     # urls for MenuElements
#     path('main/menuelements/', views.MenuElementsListView.as_view(), name='main_menuelements_list'),
#     path('main/menuelements/create/', views.MenuElementsCreateView.as_view(), name='main_menuelements_create'),
#     path('main/menuelements/detail/<int:pk>/', views.MenuElementsDetailView.as_view(), name='main_menuelements_detail'),
#     path('main/menuelements/update/<int:pk>/', views.MenuElementsUpdateView.as_view(), name='main_menuelements_update'),
# )
#
# urlpatterns += (
#     # urls for TableNodes
#     path('main/tablenodes/', views.TableNodesListView.as_view(), name='main_tablenodes_list'),
#     path('main/tablenodes/create/', views.TableNodesCreateView.as_view(), name='main_tablenodes_create'),
#     path('main/tablenodes/detail/<int:pk>/', views.TableNodesDetailView.as_view(), name='main_tablenodes_detail'),
#     path('main/tablenodes/update/<int:pk>/', views.TableNodesUpdateView.as_view(), name='main_tablenodes_update'),
# )
#
# urlpatterns += (
#     # urls for CustomerOrders
#     path('main/customerorders/', views.CustomerOrdersListView.as_view(), name='main_customerorders_list'),
#     path('main/customerorders/create/', views.CustomerOrdersCreateView.as_view(), name='main_customerorders_create'),
#     path('main/customerorders/detail/<int:pk>/', views.CustomerOrdersDetailView.as_view(), name='main_customerorders_detail'),
#     path('main/customerorders/update/<int:pk>/', views.CustomerOrdersUpdateView.as_view(), name='main_customerorders_update'),
# )
#
# urlpatterns += (
#     # urls for RestaurantInfo
#     path('main/restaurantinfo/', views.RestaurantInfoListView.as_view(), name='main_restaurantinfo_list'),
#     path('main/restaurantinfo/create/', views.RestaurantInfoCreateView.as_view(), name='main_restaurantinfo_create'),
#     path('main/restaurantinfo/detail/<int:pk>/', views.RestaurantInfoDetailView.as_view(), name='main_restaurantinfo_detail'),
#     path('main/restaurantinfo/update/<int:pk>/', views.RestaurantInfoUpdateView.as_view(), name='main_restaurantinfo_update'),
# )
#
# urlpatterns += (
#     # urls for UserReviews
#     path('main/userreviews/', views.UserReviewsListView.as_view(), name='main_userreviews_list'),
#     path('main/userreviews/create/', views.UserReviewsCreateView.as_view(), name='main_userreviews_create'),
#     path('main/userreviews/detail/<int:pk>/', views.UserReviewsDetailView.as_view(), name='main_userreviews_detail'),
#     path('main/userreviews/update/<int:pk>/', views.UserReviewsUpdateView.as_view(), name='main_userreviews_update'),
# )
#
# urlpatterns += (
#     # urls for KelnerBots
#     path('main/kelnerbots/', views.KelnerBotsListView.as_view(), name='main_kelnerbots_list'),
#     path('main/kelnerbots/create/', views.KelnerBotsCreateView.as_view(), name='main_kelnerbots_create'),
#     path('main/kelnerbots/detail/<int:pk>/', views.KelnerBotsDetailView.as_view(), name='main_kelnerbots_detail'),
#     path('main/kelnerbots/update/<int:pk>/', views.KelnerBotsUpdateView.as_view(), name='main_kelnerbots_update'),
# )
#
# urlpatterns += (
#     # urls for KelnerOrders
#     path('main/kelnerorders/', views.KelnerOrdersListView.as_view(), name='main_kelnerorders_list'),
#     path('main/kelnerorders/create/', views.KelnerOrdersCreateView.as_view(), name='main_kelnerorders_create'),
#     path('main/kelnerorders/detail/<int:pk>/', views.KelnerOrdersDetailView.as_view(), name='main_kelnerorders_detail'),
#     path('main/kelnerorders/update/<int:pk>/', views.KelnerOrdersUpdateView.as_view(), name='main_kelnerorders_update'),
# )
