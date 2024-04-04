from django.urls import path

from .views import (
    IncomingCreateView,
    IncomingDetailView,
    IncomingListView,
    IncomingUpdateView,
)

urlpatterns = [
    path("", IncomingListView.as_view(), name="incoming-list"),
    path("detail/<int:pk>/", IncomingDetailView.as_view(), name="incoming-detail"),
    path("update/<int:pk>/", IncomingUpdateView.as_view(), name="incoming-update"),
    path("add-new/", IncomingCreateView.as_view(), name="incoming-create"),
]
