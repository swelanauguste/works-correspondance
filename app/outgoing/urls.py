from django.urls import path

from .views import (
    OutgoingCreateView,
    OutgoingDetailView,
    OutgoingListView,
    OutgoingUpdateView,
)

urlpatterns = [
    path("", OutgoingListView.as_view(), name="outgoing-list"),
    path("detail/<int:pk>/", OutgoingDetailView.as_view(), name="outgoing-detail"),
    path("update/<int:pk>/", OutgoingUpdateView.as_view(), name="outgoing-update"),
    path("add-new/", OutgoingCreateView.as_view(), name="outgoing-create"),
]
