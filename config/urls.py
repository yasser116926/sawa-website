from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('projects/', include('projects.urls')),
    path('research/', include('research.urls')),
    path('events/', include('events.urls')),
    path('sitemap/', include('sitemap.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('feed/', include('feed.urls')),
]
