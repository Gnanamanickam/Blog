from blog import views
from django.urls import include
from django.contrib import admin

from django.urls import path
from blog.feed import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]