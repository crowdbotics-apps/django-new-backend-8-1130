from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    GhhViewSet,
    HomePageViewSet,
    HomePage1ViewSet,
    R1xViewSet,
    R2d2ViewSet,
    RX2ViewSet,
    RX3ViewSet,
    RxxxViewSet,
    XT1ViewSet,
    XT2ViewSet,
    XT3ViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
    AppReportView,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, base_name="signup")
router.register("login", LoginViewSet, base_name="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("homepage1", HomePage1ViewSet)
router.register("r1x", R1xViewSet)
router.register("r2d2", R2d2ViewSet)
router.register("rx2", RX2ViewSet)
router.register("rx3", RX3ViewSet)
router.register("ghh", GhhViewSet)
router.register("rxxx", RxxxViewSet)
router.register("xt1", XT1ViewSet)
router.register("xt2", XT2ViewSet)
router.register("xt3", XT3ViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report", AppReportView.as_view(), name="app_report"),
]
