from django.conf.urls import url

from . import views

urlpatterns = [

    url(r"^index/$", views.index, name='index'),
    url(r"^name/$", views.name, name='name'),
    url(r"^terms_privacy/$", views.terms_privacy, name='terms_privacy'),
    url(r"^searchPage/$", views.searchPage, name='searchPage'),
    url(r"^signup/$", views.signup, name='signup'),
    url(r"^meal/$", views.meal, name='meal'),
    url(r"^our_suggestion/$", views.our_suggestion, name='our_suggestion'),
    url(r"^not_that_expensive/$", views.not_that_expensive, name='not_that_expensive'),
    url(r"^something_fast/$", views.something_fast, name='something_fast'),
    url(r"^something_healthy/$", views.something_healthy, name='something_healthy'),
    url(r"^select_mood/$", views.select_mood, name='select_mood'),
    url(r"^favorite/$", views.favorite, name='favorite'),
    url(r"^logout_page/$", views.logout_page, name='logout_page'),


]
