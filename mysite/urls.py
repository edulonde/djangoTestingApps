from django.contrib import admin
from django.urls import include, path

from listings.views import (
    listing_list,
    listing_retrieve,
    listing_create,
    listing_update,
    listing_delete,
)

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('listings/', listing_list),
    path('listings/<pk>/', listing_retrieve),
    path('add-listing/', listing_create),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete),
    path("__reload__/", include("django_browser_reload.urls")),

]
