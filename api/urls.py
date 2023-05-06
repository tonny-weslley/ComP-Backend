from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core.views import (CategoryViewSet, ProductViewSet, RegisterViewSet,
                        StoreViewSet, UserViewSet, VariationViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'variations', VariationViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'registers', RegisterViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
