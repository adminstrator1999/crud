from django.urls import path, re_path
from .views import table, reg, add, delete, view, edit, edition, search, university, add_university, \
    add_university_page, tabl, update_student

urlpatterns = [
    path('', table, name='table'),
    path('reg/', reg, name='reg'),
    path('add/', add, name='add'),
    re_path('^delete/(?P<id>\d+)/$', delete, name='delete'),
    re_path('^view/(?P<id>\d+)/$', view, name='view'),
    re_path('^edit/(?P<id>\d+)/$', edit, name='edit'),
    path('edition/', edition, name='edition'),
    re_path('search/', search, name='search'),
    path('university/', university, name='university'),
    path('add_university_page/', add_university_page, name='add_university_page'),
    path('add_university', add_university, name='add_university'),
    path('add_student', tabl, name='add_student'),
    path('update_student/<str:pk>/', update_student, name='update_student'),
]
