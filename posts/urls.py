from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls