from django.urls import path

from carworld.vehicles.views import VehicleDetailsView, CommentVehicleView, ListVehiclesView, \
    CreateVehicleView, EditVehicleView, DeleteVehicleView, LikeVehicleView

urlpatterns = [
    path('', ListVehiclesView.as_view(), name='list vehicles'),
    path('details/<int:pk>', VehicleDetailsView.as_view(), name='vehicle details'),
    path('like/<int:pk>', LikeVehicleView.as_view(), name='like vehicle'),
    path('create/', CreateVehicleView.as_view(), name='create vehicle'),
    path('edit/<int:pk>', EditVehicleView.as_view(), name='edit vehicle'),
    path('delete/<int:pk>', DeleteVehicleView.as_view(), name='delete vehicle'),
    path('comment/<int:pk>', CommentVehicleView.as_view(), name='comment vehicle'),
]
