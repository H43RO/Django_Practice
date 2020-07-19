from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField() ## 길이 제한 없는 긴 문자열

    created_at = models.DateTimeField(auto_now_add=True) ## 게시글 생성될 때 자동으로 현재 시간 기록
    updated_at = models.DateTimeField(auto_now=True) ## 게시글 수정될 때 자동으로 현재 시간 기록

    # num = models.IntegerField() ## 숫자 필드는 이렇게 선언함

