# STATIC

## STATIC_ROOT

- 배포할 때 사용
- 개발할 때 사용할 일 X
- python manage.py collectstatic => 모든 static 파일을 한 곳으로 모아주는 명령어
- **그 모든 파일을 "어디에" 모을 건지 지정하는 변수**



## STATIC_URL

- 내 컴퓨터에 있는 정적 파일(JS, CSS, images)을 **외부에서 접근할 수 있게끔 URL을 부여해줄 때** 사용하는 prefix

- `http://localhost:8000/static/example.png`



## STATICFILES_DIRS

> TEMPLATES => DIRS = [] 와 같음

- Django는 기본적으로 모든 정적 파일을 찾을 때 각 앱의 static이라는 이름의 폴더를 찾음
- **앱 안의 static 폴더 말고, 외부에 별도의 경로를 지정해주고 싶을 때 사용하는 리스트(또는 변수)**



## MEDIA_ROOT

- 사용자가 올리는 파일을 저장하는 경롤르 지정하는 변수



## MEDIA_URL

- static_url과 동일
- 사용자가 올린 파일들에만 적용됨