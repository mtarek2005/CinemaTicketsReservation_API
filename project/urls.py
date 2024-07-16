from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="authentication/password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="users_hub/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users_hub/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users_hub/password_reset_complete.html'), name='password_reset_complete'),
    
    path('django/jsonresponsenomodel/', views.no_rest_no_model),
    
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    
    path('rest/fbv/', views.FBV_List),
    path('rest/fbv2/', views.FBV_List2),
    
    path('rest/fbv/<int:pk>', views.FBV_pk),
    
    path('rest/cbv/', views.CBV_List.as_view()),
    
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),
    
    path('rest/generics/', views.generics_list.as_view()),
    
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),
    
    path('rest/viewsets/', include(router.urls)),
    
    path('fbv/findmovie', views.find_movie),
    
    path('fbv/newreservation',views.new_reservation),
    
    path('api-auth', include('rest_framework.urls')),
    
    path('api-token-auth', obtain_auth_token),
    
    path('post/generics/<int:pk>', views.Post_pk.as_view()),
    path('ratings/<int:pk>', views.ratings),
    path('avg_rating/<int:pk>', views.avg_rating),
]
