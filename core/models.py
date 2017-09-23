from django.db import models
from django.urls import reverse_lazy, reverse

from model_utils.models import SoftDeletableModel

from .managers import PessoaManager


class Pessoa(SoftDeletableModel):
    nome = models.CharField(max_length=255)
    objects = PessoaManager()

    def __str__(self):
        return 'Pessoa: {} - Nome: {} - is_removed: {}'.format(self.pk, self.nome, self.is_removed)

    @property
    def delete_url(self):
        if self.pk:
            return reverse_lazy('pessoa-delete', kwargs={'pk': self.pk})
        else:
            return None

    @property
    def update_url(self):
        if self.pk:
            return reverse_lazy('pessoa-update', kwargs={'pk': self.pk})
        else:
            return None

    @property
    def detail_url(self):
        if self.pk:
            return reverse_lazy('pessoa-detail', kwargs={'pk': self.pk})
        else:
            return None

    @property
    def list_url(self):
        if self.pk:
            return reverse('pessoa-list')
        else:
            return None

    def delete(self, using=None, soft=True, *args, **kwargs):
        print('passou aqui')
        return super().delete(using, soft, *args, **kwargs)
