from django.views.generic import FormView
from .models import Services, Team
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(FormView):
    template_name: str = 'index.html'
    form_class: str = ContactForm
    success_url: str = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        context['team'] = Team.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "Email has been successfully sended!")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Error to send e-mail")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
