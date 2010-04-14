urlpatterns = patterns('',
    (r'^$', 'blog.views.index'),
    (r'staring/$','starrating.views.star'),
)
