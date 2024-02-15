from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # when the root URL (empty string "") is accessed, 
    # the index function from the views module should handle the request.
    path("", views.IndexView.as_view(), name="index"),
    # path(route, views.function, kwargs, name)
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultView.as_view(), name='results'),
    path("<int:question_id>/vote/",views.vote, name='vote'),
]