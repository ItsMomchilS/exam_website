from django.urls import path

from carworld.others.views import ListSourcesView, CreateSourceView, DeleteSourceView, EditSourceView, SourceDetailsView

urlpatterns = (
    path('', ListSourcesView.as_view(), name='list sources'),
    path('create/', CreateSourceView.as_view(), name='create source'),
    path('edit/<int:pk>', EditSourceView.as_view(), name='edit source'),
    path('delete/<int:pk>', DeleteSourceView.as_view(), name='delete source'),
    path('details/<int:pk>', SourceDetailsView.as_view(), name='source details'),
)
