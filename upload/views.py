from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from upload.models import Document


class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload' ]
    success_url = reverse_lazy('home')
    template_name = 'upload/document_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)