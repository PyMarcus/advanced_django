from django.views.generic import TemplateView
from .models import Services, Team


class IndexView(TemplateView):
    template_name: str = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        context['team'] = Team.objects.all()
        return context
