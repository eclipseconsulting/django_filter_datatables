from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.CustomerFilterView.as_view(), name='customer_search'),
    path('<pk>/detail', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('<pk>/edit', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('new', views.CustomerCreateView.as_view(), name='customer_create'),
    path('<pk>/delete', views.CustomerDeleteView.as_view(), name='customer_delete'),
]
