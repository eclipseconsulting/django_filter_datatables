from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views import View
from django.views.generic import UpdateView, CreateView, DetailView

from apps.utils.views import FilterView
from . import forms, filters, models, helpers


class CustomerFilterView(LoginRequiredMixin, FilterView):
    sorting = {0: ['last_name'], 1: ['first_name']}
    values = ('pk',)
    object_class = models.Customer
    filter_class = filters.CustomerFilter
    template_name = 'customers/customer_filter.html'

    @staticmethod
    def result_function(qs):
        result = []

        for b in qs:
            object = models.Customer.objects.get(pk=b['pk'])
            col = {"last_name": helpers.format_link(object.get_absolute_url(), object.last_name),
                   "first_name": object.first_name}
            result.append(col)
        return result


class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'customers/customer_detail.html'
    queryset = models.Customer.objects.all()


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'customers/customer_update.html'
    queryset = models.Customer.objects.all()
    form_class = forms.CustomerForm


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'customers/customer_update.html'
    model = models.Customer
    form_class = forms.CustomerForm


class CustomerDeleteView(LoginRequiredMixin, View):
    object_class = models.Customer

    def get(self, request, pk):
        object = get_object_or_404(self.object_class, pk=pk)
        edit_url = reverse('customers:customer_update', kwargs={'pk': pk})
        return render(
            request,
            'generic_confirm_delete.html',
            {'object': object, 'title': 'Customer', 'cancel_url': edit_url},
        )

    def post(self, request, pk):
        object = get_object_or_404(self.object_class, pk=pk)
        object.delete()
        return redirect('customers:customer_search')
