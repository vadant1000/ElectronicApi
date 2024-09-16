from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from school_app import views as school_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', school_views.UsersViewSet)
router.register(r'order', school_views.OrdersViewSet)
router.register(r'group', school_views.GroupsViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)