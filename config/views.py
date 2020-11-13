# view : 기능을 담당 (페이지 단위, 로그인페이지, 제품목록 페이지 등등 ... )
# 화면이 나타나는 뷰(템플릿 있는 뷰), 화면이 없는 뷰(템플릿이 없을 수 있는 뷰)
# 화면이 있는 뷰 - 로그인 페이지
# 화면이 없는 뷰 - 에이작스 콜하는 뷰
# 화면이 있건 없건 주소 URL 은 있어야 한다.

# 뷰 내용(함수, 클래스), URL 이 있으면 동작한다.

# 뷰의 코드 형식 : 함수형, 클래스형

# 함수형 - request 를 매개변수로 받고(추가 매개변수 가능), 모양은 함수,
#        내가 원하는대로 동작들을 설계하고 만들고 싶을 때

# 클래스형 - CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고,
#          상속받아서 사용한다.
# 장고의 제네릭 뷰를 많이 사용

from django.http import HttpResponse

def index(request):
    # 요청한 내용들 - 세션 , 쿠키 등등
    # 어떤 계산이나, 데이터 베이스 조회, 수정, 등록
    # 응답 메세지를 만들어서 반환.
    html = '<html><body>Hello! django</body><html>'
    return HttpResponse(html)

# 뷰의 이름은 welcome
# 접속주소  - welcome/
# 내용은 : Welcome to Django.

def welcome(request):
    html = '<html><body>Welcome to Django.</body><html>'
    return HttpResponse(html)
