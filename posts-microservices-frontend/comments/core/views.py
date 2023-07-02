from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CommentSerializer
from rest_framework.views import APIView
from .models import Comment
import requests


class PostCommentAPIView(APIView):
    def get(self, _, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        comment = serializer.data
        r = requests.post('http://127.0.0.1:8000/api/posts/%d/comments' % comment['post_id'], data={
            'text': comment['text']
        })

        if not r.ok:
            # do something
            pass

        return Response(comment)
