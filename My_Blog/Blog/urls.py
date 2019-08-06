from django.urls import path
from . import  views
urlpatterns =[
        path('',views.index,name='home'),
        path('about/',views.about,name='about'),
        path('post_details/<int:post_id>/',views.post_details,name='post_details'),
        path('new_Post/',views.PostCreateView.as_view(),name='new_post'),
        path('post_details/<slug:pk>/update/',views.PostUpdateView.as_view(),name='post_update'),
        # slug must use pk not id
        path('post_details/<slug:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),




    ]
