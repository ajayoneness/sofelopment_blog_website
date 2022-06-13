from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('adminlogin/',views.adminlogin,name="adminLogin"),
    path('createpost/',views.createPost,name='createpost'),
    path('draft/',views.draft,name="draft"),
    path('cat/<str:aj>',views.cat, name="cat"),
    path('showall/',views.showall,name='showall'),
    path("delete/<int:obj>",views.delete,name='delete'),
    path("edit/<int:id>",views.edit,name='edit')

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

