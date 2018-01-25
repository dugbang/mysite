## 장고 연습 프로젝트

* 장고를 학습하면서 발생하는 모든 연습코드를 본 프로젝트에 기록한다.

1. [Python + Django 서버 구축하기](https://www.gitbook.com/book/javafa/python-django/details)
    - app; memo
    - app; bbs
        - Rest Framework 사용
        - 포스트맨을 통한 데이터 입출력 확인
1. [예제로 배우는 Python 프로그래밍 - 장고 기초](http://pythonstudy.xyz/python/article/301-Django-%EC%86%8C%EA%B0%9C)
    - app; home
    - app; feedback
        - [API 구성 - 추가, 삭제 등](http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API)
1. [장고를 활용한 쉽고 빠른 웹 개발](http://www.hanbit.co.kr/store/books/look.php?p_code=B7703021280)
    - app; bookmark
    - app; blog
    - app; /
    - [웹사이트](https://kimdoky.github.io/tags/django.html)
        - 도서의 내용이 그대로 정리되어 있음.
1. [장고 튜토리얼](https://docs.djangoproject.com/ko/2.0/intro/tutorial01/)
    - app; polls
        - 테스트 방법에 대한 설명이 있음.

## 확인해야 할 정보

* [장고 테이블 지우고 난 후 다시 마이그레이션 하는 방법!](http://forybm.tistory.com/2)
    1. 해당 앱에 있는 migrations 폴더 삭제, 단 __init__.py 파일을 제외하고 삭제하기!
    2. database에 직접 접속하여 테이블 중 django_migrations 라는 테이블에서 해당 앱에 대한 raw를 삭제.
        - DELETE FROM django_migrations WHERE app = '앱 이름'
        - **앱에 해당되는 테이블 삭제**
    3. 디비 재설정
        - python3 manage.py makemigrations
        - python3 manage.py migrate
            - python3 manage.py migrate --fake <앱이름>
