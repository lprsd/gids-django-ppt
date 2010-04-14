def post(request,post_id):
    post = Post.objects.get(pk=post_id)
    if req.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment = comment_form.save()
    payload = {'post':post,
               'comments':
               Comment.objects.filter(post__id=post_id),
               'comment_form':CommentForm()}
    return render_to_response('post.html',
                              payload,
                              RequestContext(req))    

    
