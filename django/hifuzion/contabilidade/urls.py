from rest_framework import routers

from hifuzion.contabilidade.views import ClienteViewSet, PlanoContaViewSet

router = routers.DefaultRouter()

router.register('clientes', ClienteViewSet)
router.register('planocontas', PlanoContaViewSet)

urlpatterns = router.urls
