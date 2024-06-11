from rest_framework.serializers import ModelSerializer
from app.models import *



class UserApi(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone', 'affiliatione', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class MemberApi(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class SectionApi(ModelSerializer):
    class Meta:
        model = ConferenceSection
        fields = '__all__'




class AgendaPartApi(ModelSerializer):
    class Meta:
        model = PartAgenda
        fields = '__all__'




class AgendaApi(ModelSerializer):
    parts = AgendaPartApi(many=True, read_only=True)

    class Meta:
        model = ConferenceAgenda
        fields = ['id', 'day', 'created_at', 'parts']

