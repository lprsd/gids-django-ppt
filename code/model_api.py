>>>from blog.models import Post, Comment
>>>post = Post.objects.all()[0]
>>>post_comments = post.comment_set.all()
