from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import OutgoingForm
from .models import Outgoing


class OutgoingUpdateView(UpdateView):
    model = Outgoing
    form_class = OutgoingForm


class OutgoingCreateView(CreateView):
    model = Outgoing
    form_class = OutgoingForm


class OutgoingDetailView(DetailView):
    model = Outgoing


class OutgoingListView(ListView):
    model = Outgoing
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data_count"] = Outgoing.objects.count()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Outgoing.objects.filter(
                Q(subject__icontains=query)
                | Q(out_from__icontains=query)
                | Q(to__icontains=query)
                | Q(cc__icontains=query)
                | Q(notes__icontains=query)
                # Assuming action has a name field you want to search
            ).distinct()
        return super().get_queryset()
