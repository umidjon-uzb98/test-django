from django.urls import path
from myapp.views import all_product, completed_product, waiting_product


urlpatterns = [
    path('all-product/', all_product),
    path('completed-product/', completed_product),
    path('waiting-product/', waiting_product),
#  path('app_hello_url', hello_world),
#  path('', hello_world),
#  path('app_bye_url', good_bye)
]
