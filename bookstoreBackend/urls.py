from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

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
from users.views import ReaderViewSet

router = routers.DefaultRouter()
router.register(r'analysis', AnalysisViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)
router.register(r'information', InformationViewSet)
router.register(r'note', NoteViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'tag', TagViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'reader', ReaderViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
]
