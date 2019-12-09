from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('priv_error', views.priv_error, name='priv_error'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)