from django.conf.urls import patterns, url
from ed_news import views

urlpatterns = patterns('',
    # My urls

    # --- Educator News home page ---
    url(r'^$', views.index, name='index'),

    url(r'^new/', views.new, name='new'),
    url(r'^submit_link/', views.submit_link, name='submit_link'),
    url(r'^submit_textpost/', views.submit_textpost, name='submit_textpost'),
    url(r'^upvote_submission/(?P<submission_id>\d+)/$', views.upvote_submission, name='upvote_submission'),
    url(r'^discuss/(?P<submission_id>\d+)/$', views.discuss, name='discuss'),
    url(r'^upvote_comment/(?P<comment_id>\d+)/$', views.upvote_comment, name='upvote_comment'),
    url(r'^downvote_comment/(?P<comment_id>\d+)/$', views.downvote_comment, name='downvote_comment'),
    url(r'^reply/(?P<submission_id>\d+)/(?P<comment_id>\d+)/$', views.reply, name='reply'),
    url(r'^flag_comment/(?P<submission_id>\d+)/(?P<comment_id>\d+)/$', views.flag_comment, name='flag_comment'),
    url(r'^flag_submission/(?P<submission_id>\d+)/$', views.flag_submission, name='flag_submission'),

    # --- My admin pages ---
)
