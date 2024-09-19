from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes),
    path('book/', getBooks),
    path('books/<int:pk>', getBook),


]
