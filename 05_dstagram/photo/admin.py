from django.contrib import admin

# Register your models here.

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author'] # Add thoto 할때 셀렉트가 아니고 찾기형태로 바뀜
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created', 'author__username'] # icontains author만 쓰게되면 객체이기 때문에 안됨 // __~ 하위 객체
    ordering = ['-updated', '-created'] # - 이 붙게되면 내림차순 , 없으면 오름차순

admin.site.register(Photo, PhotoAdmin)
