from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import dash_app_code
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Using Django default authentication system
    path('', include('django.contrib.auth.urls')),
	url('^dash_plot$', TemplateView.as_view(template_name='dash_plot.html'), name="dash_plot"),
	url('^django_plotly_dash/', include('django_plotly_dash.urls')),
    # Call home.html from templates folder
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]