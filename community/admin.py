from django.contrib import admin

from community.models import FreePost1, FreePicturePost


# admin.site.register(FreePost1) 이것이기본
# 응용 django강의에 나온방법
@admin.register(FreePost1)
class FreePostAdmin1(admin.ModelAdmin):
    pass

@admin.register(FreePicturePost)
class FreePicturePostAdmin(admin.ModelAdmin):
    pass
