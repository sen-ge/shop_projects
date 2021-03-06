"""shop_projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include

from apps.home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    # 设置默认首页
    url('^$',views.index),
    url('home/',include('apps.home.urls')),
    url('account/',include('apps.account.urls')),
    url('cate/',include('apps.cate_detail.urls')),
    url('car/', include('apps.cart.urls')),
    url('pay/', include('apps.pay.urls')),
    url('shop/', include('apps.shop_detail.urls')),
]
