from django.urls import path
from . import views


urlpatterns = [
    path('', views.library_home, name='library_home'),
    path('createLib', views.createLib, name='createLib'),
    path('<int:pk>', views.LibraryDetailView.as_view(), name='library-detail'),
    path('<int:pk>/update', views.LibraryUpdateView.as_view(), name='library-update'),
    path('<int:pk>/remove', views.LibraryDeleteView.as_view(), name='library-delete'),
    path('<int:pk>/createBook', views.createBook, name='createBook'),
    path('<int:pk>/<int:book_id>/update', views.BookUpdateView.as_view(), name='book-update'),
    path('<int:library_id>/<int:book_id>/delete', views.BookDeleteView.as_view(), name='book-delete'),
]
