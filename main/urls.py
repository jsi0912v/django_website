from django.urls import path
from main.views import index, posting, blog, new_post, remove_post

# images upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('blog/<int:pk>/', posting, name="posting"),
    path('blog/new_post', new_post),
    path('blog/<int:pk>/remove/', remove_post),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

