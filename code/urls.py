urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^$', 'blog.views.index'),
    (r'staring/(?P<post_id>\d+)/$',
    'starrating.views.star'),
)
