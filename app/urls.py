from django.urls import path
from app.views import Signin, Signup, MembersView, SectionView, ConferenceAgendaView


urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('signin/', Signin.as_view(), name='signin'),
    path('member/', MembersView.as_view(), name='members'),
    path('section/', SectionView.as_view(), name='sections'),
    path('agenda/', ConferenceAgendaView.as_view(), name='agenda'),
]
