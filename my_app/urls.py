from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from . import views
from login import views as v
from userlist import views as userlistviews

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', v.register, name='register'),
    path("logout", v.logout_request, name="logout"),
    path('recommendation_system', views.recommendation_system, name='recommendation_system'),
    path('search/', views.search, name='search'),
    path('search/search_genre/<str:genre>/', views.search_genre, name='search_genre'),
    path('account/', views.account, name='account'),
    path('add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist, name='add_to_animelist'),
    path('add_to_animelist_recommendation/<int:id>/<int:like>/', userlistviews.add_to_animelist_recommendation, name='add_to_animelist_recommendation'),
    path('search/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist, name='add_to_animelist'),
    path('search/search_genre/Action/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Cars/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Comedy/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Dementia/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Demons/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Drama/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Ecchi/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Fantasy/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Game/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Harem/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Historical/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Horror/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Josei/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Kids/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Magic/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Martial_Arts/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Mecha/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Military/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Music/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Mystery/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Parody/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Police/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Psychological/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Romance/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Samurai/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/School/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Sci-Fi/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Seine/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Shoujo/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Shoujo_Ai/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Shounen/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Shounen_ai/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Slice_of_Life/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Space/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Sports/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Super_Power/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Supernatural/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Thriller/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('search/search_genre/Vampire/add_to_animelist/<int:id>/<int:like>/', userlistviews.add_to_animelist,
         name='add_to_animelist'),
    path('account/delete_to_animelist/<int:anime_id>/', userlistviews.delete_to_animelist, name='delete_to_animelist'),

]