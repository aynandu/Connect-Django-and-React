from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MyModelView

router=DefaultRouter()
router.register(r'mymodels',MyModelView)

urlpatterns = [
    path('',include(router.urls)),
]
