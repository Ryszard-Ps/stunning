from django.conf.urls import url

from .views import (RestaurantCreation, RestaurantDelete, RestaurantDetail,
                    RestaurantList, RestaurantUpdate)

urlpatterns = [
    url(r'^$', RestaurantList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', RestaurantDetail.as_view(), name='detail'),
    url(r'^new$', RestaurantCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', RestaurantUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', RestaurantDelete.as_view(), name='delete'),

]
