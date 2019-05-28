from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', myapp.views.new, name="new"),
    path('', myapp.views.index, name="index"),
    path('<int:diary_id>', myapp.views.detail, name="detail"),
    path('myapp/edit/<int:diary_id>', myapp.views.edit, name="edit"),
    path('myapp/delete/<int:diary_id>', myapp.views.delete, name="delete"),
    path('signup/', myapp.views.signup, name="signup"),
    path('login/', myapp.views.login, name="login"),
    path('logout/', myapp.views.logout, name="logout"),
    path('<int:diary_id>/comment/create', myapp.views.comment_create, name="comment_create"),
    path('<int:diary_id>/comment/<int:comment_id>/delete', myapp.views.comment_delete, name="comment_delete"),
    path('<int:diary_id>/comment/<int:comment_id>/edit', myapp.views.comment_edit, name="comment_edit"),

    
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

