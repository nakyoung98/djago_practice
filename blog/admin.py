from django.contrib import admin

# 관리자 페이지에 Post 모델 추가하기 1
from .models import Post

# Register your models here.
# 관리자 페이지에 Post 모델 추가하기 2 -> 관리자 페이지에 blog라는 섹션이 생기고, post라는 메뉴가 생김.
admin.site.register(Post)