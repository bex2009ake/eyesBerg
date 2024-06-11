from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from app.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from app.serializers import *
from django.db.models import Prefetch



class Signup(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Signup'})
    
    def post(self, req: Request):
        user = User.objects.create_user(
            first_name = req.data.get('first_name'), 
            last_name = req.data.get('last_name'), 
            email = req.data.get('email'), 
            gender = req.data.get('gender'), 
            phone  = req.data.get('phone'), 
            affiliatione = req.data.get('affiliatione'), 
            password  = req.data.get('password'),
        )
        
        token = RefreshToken.for_user(User)

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        })
    



class Signin(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Signin'})
    
    def post(self, req: Request):
        email = req.data.get('email')
        password = req.data.get('password')

        user = User.objects.get(email=email)

        if not user.check_password(password):
            return Response({'error': 'Wrong password !!!'})

        token = RefreshToken.for_user(User)        

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        })
    

class MembersView(APIView):
    def get(self, req: Request):
        members = Member.objects.all()
        serializer = MemberApi(members, many=True)
        return Response(serializer.data)
    
    def post(self, req: Request):
        member_serializer = MemberApi(data=req.data)
        if member_serializer.is_valid():
            member_serializer.save()
            return Response(member_serializer.data)
        else:
            return Response(member_serializer.errors)
        

class SectionView(APIView):
    def get(self, req: Request):
        members = ConferenceSection.objects.all()
        serializer = SectionApi(members, many=True)
        return Response(serializer.data)
    
    def post(self, req: Request):
        member_serializer = SectionApi(data=req.data)
        if member_serializer.is_valid():
            member_serializer.save()
            return Response(member_serializer.data)
        else:
            return Response(member_serializer.errors)
        


class ConferenceAgendaView(APIView):
    def get(self, req: Request):
        agena = ConferenceAgenda.objects.prefetch_related(Prefetch('parts', queryset=PartAgenda.objects.all())) 

        serializer = AgendaApi(agena, many=True)
        return Response(serializer.data)
    
    def post(self, req: Request):
        agena = ConferenceAgenda.objects.create(day=req.data.get('day'))
        
        parts = req.data.getlist('parts')

        for i in parts:
            PartAgenda.objects.create(agend=agena, title=i)

        return Response({'msg': 'Successful !!!'})
        