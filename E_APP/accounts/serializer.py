from rest_framework import serializers
from .models import Profile
from rest_framework_simplejwt.tokens import RefreshToken

class Profile_serializer(serializers.ModelSerializer):
    user_email = serializers.EmailField()
    class Meta:
        model = Profile
        fields = ['name','username','user_email','password']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Profile
        fields = ['user_email','password']

    def validate(self, data):
        password = data['password']
        email = data['email']

        if not  Profile.objects.filter(user_email=email,password=password).exists():
            raise serializers.ValidationError('invalid username or password')
        return data


    def get_jwt_token(self,data):

        user =  Profile.objects.get(user_email = data['email'],password = data['password'])
        if not user:
            return {'msg':'user not found'}

        refresh = RefreshToken.for_user(user)

        return {
            'msg':'login successfully',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class ForgotPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Profile
        fields = ['email']

    def validate(self, data):
        email = data['email']

        obj = Profile.objects.filter(user_email=email)
        if not obj.exists():
            raise serializers.ValidationError('email is not valid')
        return data