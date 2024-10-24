from django.urls import path, include
from chatapp import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path("chat/", chat_views.chatPage, name="chat-page"),

    # # login-section
    # path("auth/login/", LoginView.as_view
    #      (template_name="chat/LoginPage.html"), name="login-user"),
    # path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path("inbox/<user_id>/", views.MyInbox.as_view()),
    path("inbox/<sender_id>/<reciever_id>/", views.GetMessages.as_view()),
    path("send_messages/", views.SendMessage.as_view()),
    path("search/<name>/", views.SearchUser.as_view()),

    #
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]