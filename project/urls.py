from django.contrib import admin
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
    
    path('django/jsonresponsenomodel/', views.no_rest_no_model),
    
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    
    path('rest/fbv/', views.FBV_List),
    
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
]
