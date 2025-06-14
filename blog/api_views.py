from blog.api.serializers import PostSerializer

def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return JsonResponse({"data": PostSerializer(posts, many=True).data})

    if request.method == "POST":
        post_data = json.loads(request.body)
        serializer = PostSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return JsonResponse(PostSerializer(post).data)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        return JsonResponse(PostSerializer(post).data)

    if request.method == "PUT":
        post_data = json.loads(request.body)
        serializer = PostSerializer(post, data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(PostSerializer(post).data)
