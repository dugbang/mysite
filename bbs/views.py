from django.shortcuts import render

# Create your views here.

# 클래스 기반의 Rest CRUD 처리
from bbs.models import Bbs
from bbs.serializers import BbsSerializer
from rest_framework import generics


# generics 에 목록과 생성 API 가 정의되어 있다
class BbsList(generics.ListCreateAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer


# generics 에 상세, 수정, 삭제 API가 정의되어 있다
class BbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer

