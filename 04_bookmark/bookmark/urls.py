from django.urls import path
from .views import BookmarkListView, BookmarkCreateView
urlpatterns = [
    # http://127.0.0.1/bookmark/
    # ???
    # 클래스 뷰로 사용할 경우 .as_view() 를 꼭 사용해야함 !
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),

]