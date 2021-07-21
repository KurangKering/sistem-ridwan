from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from fcm.models import DataLatihPemain
from django.db.models import Q

import functools
import operator

class DataLatihPemainTengahDataTables(BaseDatatableView):
    # The model we're going to show
    model = DataLatihPemain

    # define the columns that will be returned
    columns = ['id', 'nama', 'usia', 'pemain_inti', 'cadangan_main', 'mop', 'kk', 'km', 'gol', 'assist', 'pelanggaran', 'dilanggar_lawan', 'akurasi_tembakan', 'akurasi_operan', 'akurasi_umpan_silang', 'sukses_dribel']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['id', 'nama', 'usia', 'pemain_inti', 'cadangan_main', 'mop', 'kk', 'km', 'gol', 'assist', 'pelanggaran', 'dilanggar_lawan', 'akurasi_tembakan', 'akurasi_operan', 'akurasi_umpan_silang', 'sukses_dribel']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def get_initial_queryset(self):
        return DataLatihPemain.get_posisi_depan()

    def render_column(self, row, column):
        # # We want to render user as a custom column
        # if column == 'user':
        #     # escape HTML for security reasons
        #     return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
        # else:
        return super(DataLatihPemainTengahDataTables, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        lookups = [
            'id__istartswith',
            'nama__istartswith',
            'usia__istartswith',
            'pemain_inti__istartswith',
            'cadangan_main__istartswith',
            'mop__istartswith',
            'kk__istartswith',
            'km__istartswith',
            'gol__istartswith',
            'assist__istartwith',
            'pelanggaran__istartwith',
            'dilanggar_lawan__istartwith',
            'akurasi_tembakan__istartwith',
            'akurasi_operan__istartwith',
            'akurasi_umpan_silang__istartwith',
            'sukses_dribel__istartwith',
        ]

        or_queries = [Q(**{lookup: search}) for lookup in lookups]


        if search:
            qs = qs.filter(functools.reduce(operator.or_, or_queries))

        # more advanced example using extra parameters
        # filter_customer = self.request.GET.get('customer', None)

        # if filter_customer:
        #     customer_parts = filter_customer.split(' ')
        #     qs_params = None
        #     for part in customer_parts:
        #         q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
        #         qs_params = qs_params | q if qs_params else q
        #     qs = qs.filter(qs_params)
        return qs
