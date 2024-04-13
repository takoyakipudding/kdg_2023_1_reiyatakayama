from django.urls import path

from .import views
 
urlpatterns = [
    path('agendapp/',views.ListInformationView.as_view(),name='agendapp'),
    path('odai/',views.ListFlipView.as_view(),name='odai'),
    path('create/', views.PhotoView.as_view(),name='create'),
    # <int:cate>/<int:pk>
] 