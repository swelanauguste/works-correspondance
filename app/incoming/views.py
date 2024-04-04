from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ActionForm, IncomingForm
from .models import Incoming


class IncomingUpdateView(UpdateView):
    model = Incoming
    form_class = IncomingForm


class IncomingCreateView(CreateView):
    model = Incoming
    form_class = IncomingForm


class IncomingDetailView(DetailView):
    model = Incoming


class IncomingListView(ListView):
    model = Incoming
    paginate_by = 10  # Optional: if you want to paginate the results

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Incoming.objects.filter(
                Q(subject__icontains=query)
                | Q(rfrom__icontains=query)
                | Q(to__icontains=query)
                | Q(cc__icontains=query)
                | Q(notes__icontains=query)
                | Q(
                    action__name__icontains=query
                )  # Assuming action has a name field you want to search
            ).distinct()
        return super().get_queryset()
