from model_utils.managers import SoftDeletableQuerySet, SoftDeletableManager


class PessoaQuerySet(SoftDeletableQuerySet):
    def removed(self):
        return self.filter(is_removed=True)


class PessoaManager(SoftDeletableManager):
    _queryset_class = PessoaQuerySet

    def removed(self):
        """
        Return queryset all, included the removed entries.
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).removed()

    def all(self, include_removed=False):
        """
        Return queryset all, included the removed entries.
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        if include_removed:
            qs = self._queryset_class(**kwargs)
        else:
            qs = self._queryset_class(**kwargs).filter(is_removed=False)
        return qs
