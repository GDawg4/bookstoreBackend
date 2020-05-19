from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from analysis.views import AnalysisViewSet
from authors.views import AuthorViewSet
from books.views import BookViewSet
from information.views import InformationViewSet
from notes.views import NoteViewSet
from publishers.views import PublisherViewSet
from reviews.views import ReviewViewSet
from series.views import SeriesViewSet
from tags.views import TagViewSet
from transactions.views import TransactionViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'analysis', AnalysisViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)
router.register(r'information', InformationViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'tags', TagViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls))
]
