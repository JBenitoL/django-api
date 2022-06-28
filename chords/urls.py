from chords import views
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", views.ChordsViewSet, basename="posts")
urlpatterns = router.urls
urlpatterns += []
