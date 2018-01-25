from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from upload.models import Document, PrivateDocument


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


class PrivateDocumentView(LoginRequiredMixin,CreateView):
    model = PrivateDocument
    fields = ['upload' ]
    success_url = reverse_lazy('home')
    template_name = 'upload/private_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = PrivateDocument.objects.filter(user=self.request.user)
        context['documents'] = documents
        return context
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
