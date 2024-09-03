from django.urls import path, include
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)
from rest_framework import routers

app_name = "cinema"

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path(
        "cinemahalls/",
        cinema_hall_list,
        name="cinema_hall_list"
    ),
    path(
        "cinemahalls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall_detail"
    ),
    path("", include(router.urls), name="movie-list"),
]
