"""soko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import duka.views
import duka.apiviews

urlpatterns = [
                  path('api/v1/products/', duka.apiviews.ProductList.as_view()),
                  path('api/v1/products/new', duka.apiviews.ProductCreate.as_view()),
                  path('api/v1/products/<int:id>/', duka.apiviews.ProductRetrieveUpdateDestroy.as_view()),
                  path('admin/', admin.site.urls),
                  path('products/<int:id>/', duka.views.show, name='show-product'),
                  path('cart/', duka.views.cart, name='shopping-cart'),
                  path('', duka.views.index, name='list-products'),
                  path('api/v1/products/<int:id>/stats', duka.apiviews.ProductStats.as_view()),
              ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
