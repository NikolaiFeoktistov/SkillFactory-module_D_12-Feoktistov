from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),# делаем так, чтобы все адреса из нашего приложения  сами автоматически подключались когда мы их добавим.
    path('sign/', include('sign.urls')),
    path('protect/', include('protect.urls')),
    path('accounts/', include('allauth.urls')),
]

