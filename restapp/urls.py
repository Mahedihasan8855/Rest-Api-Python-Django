from django.contrib import admin
from django.urls import path,include
from restapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import Route,DefaultRouter
from restapp.views import ViewSetArticleView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
router=DefaultRouter()
router.register(r'list',views.UserList)
router.register(r'list',views.UserDetails)



urlpatterns = [
    path('list/', views.ArticleList.as_view()),
    path('list/<int:pk>/', views.ArticleDetails.as_view()),
    path('generic/', views.GenericArticleview.as_view()),
    path('generic/<int:id>/', views.GenericArticleview.as_view()),
    path('users/', include(router.urls)),
    path('users/<int:id>/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),



]