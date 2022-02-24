class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        # Instantiate paginator class
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        # Paginate the data from the db
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        # paginate the serialized data gotten from db
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
