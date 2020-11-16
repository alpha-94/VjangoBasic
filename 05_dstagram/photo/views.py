from django.shortcuts import render

# Create your views here.

from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect


def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()  # objects 매니저
    return render(request, 'photo/list.html', {'objects_list': photos})  # 템플릿 폴더로부터 생김


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']  # 작성자(author), 작성시간(created)
    template_name = 'photo/upload.html'

    # 로그인 했다고 생각한 로직 / 로그인 하지 않았을 경우 따로
    def form_valid(self, form):
        # 작성자 매칭
        form.instance.author_id = self.request.user.id  # 규칙 ! (장고 매뉴얼 참고)

        if form.is_valid():
            # 데이터가 올바르다면 저장을 하겠다.
            form.instance.save()  # 모델 내 폼 팩토리 생성 / DB 에 저장 !
            return redirect('/')  # 루트로 가게 한다 .
        else:
            return self.render_to_response({'form': form})
            # 폼 객체를 돌려주지 않으면 회원가입 등 그 폼이 싹 사라짐 ..


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
