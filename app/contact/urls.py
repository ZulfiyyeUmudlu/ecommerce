# from django.urls import path
# from . import views    

# urlpatterns = [
#     path('contact', views.index,name='contact')
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),  # 'contact' görünüm fonksiyonunu 'contact/' URL'ine bağlayın
]
