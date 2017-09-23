from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import ModelFormMixin, BaseCreateView

from . import models


class FormActionViewMixin(object):
    form_action = None
    submit_message = None

    def get_submit_message(self):
        return self.submit_message or "Cadastrar"

    def get_form_action(self):
        if not self.form_action:
            raise ImproperlyConfigured(
                "%(cls)s is missing a 'form_action'. Define "
                "%(cls)s.form_action, or override "
                "%(cls)s.get_form_action()." % {
                    'cls': self.__class__.__name__
                }
            )
        return self.form_action

    def get_context_data(self, **kwargs):
        context = super(FormActionViewMixin, self).get_context_data(**kwargs)
        context['form_action'] = self.get_form_action()
        context['submit_message'] = self.get_submit_message()
        return context


class PessoaListView(FormActionViewMixin, ModelFormMixin, generic.ListView):
    model = models.Pessoa
    fields = ['nome', ]
    form_action = reverse_lazy('pessoa-create')
    success_url = reverse_lazy('pessoa-list')
    object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deletados'] = self.model.objects.removed()
        return context


class PessoaCreateView(FormActionViewMixin, generic.CreateView):
    model = models.Pessoa
    fields = ['nome', ]
    form_action = reverse_lazy('pessoa-create')

    def get_success_url(self):
        return self.object.detail_url


class PessoaDetailView(generic.DetailView):
    model = models.Pessoa


class PessoaDeleteView(FormActionViewMixin, generic.DeleteView):
    model = models.Pessoa
    submit_message = "Deletar"

    def get_success_url(self):
        return self.object.list_url

    def get_form_action(self):
        return self.object.delete_url


class PessoaUpdateView(FormActionViewMixin, generic.UpdateView):
    model = models.Pessoa
    fields = '__all__'
    submit_message = "Salvar"

    def get_success_url(self):
        return self.object.detail_url

    def get_form_action(self):
        return self.object.update_url
