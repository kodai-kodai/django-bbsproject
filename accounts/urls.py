from django.urls import path
from . import views
from bbs.views import custom_permission_denied_view

# カスタム403エラーハンドラの設定
handler403 = 'bbs.views.custom_permission_denied_view'
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]