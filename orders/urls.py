from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Orders
from . import views

router = DefaultRouter()
router.register('orders', Orders)

urlpatterns = [
    path('api/', include(router.urls)),
    path('order_form/', views.form, name='order_form'),




]
