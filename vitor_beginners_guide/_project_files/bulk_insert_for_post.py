from django.contrib.auth.models import User
from boards.models import Board, Topic, Post

user = User.objects.first()

topic = Topic.objects.get(pk=1)

for i in range(1000):
    message = 'Message test #{}'.format(i)
    Post.objects.create(message=message, topic=topic, created_by=user)