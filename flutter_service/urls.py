from django.urls import path
from flutter_service.views import create_product_flutter, login, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]