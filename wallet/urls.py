from django.urls import path
from .views import index_page, second_page, create_account

urlpatterns = [
    path('index/', index_page),
    path('second/', second_page),
    path('create-account/', create_account)
]
