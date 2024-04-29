from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import IncomingForm
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
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data_count"] = Incoming.objects.count()
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Incoming.objects.filter(
                Q(subject__icontains=query)
                | Q(rfrom__icontains=query)
                | Q(to__icontains=query)
                | Q(cc__icontains=query)
                | Q(notes__icontains=query)
                | Q(action__icontains=query)
                # Assuming action has a name field you want to search
            ).distinct()
        return super().get_queryset()
