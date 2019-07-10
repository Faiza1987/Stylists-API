from rest_framework import serializers
from api.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'years_experience', 'licenses',
                  'photo1',
                  'photo2', 'photo3', 'photo4', 'photo5', 'photo6',
                  'specializations')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name',
                  'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.phone_number = profile_data.get('phone_number',
                                                profile.phone_number)
        profile.years_experience = profile_data.get(
            'years_experience', profile.years_experience)
        profile.licenses = profile_data.get('licenses',
                                            profile.licenses)
        profile.photo1 = profile_data.get('photo1', profile.photo1)
        profile.photo2 = profile_data.get('photo2', profile.photo2)
        profile.photo3 = profile_data.get('photo3', profile.photo3)
        profile.photo4 = profile_data.get('photo4', profile.photo4)
        profile.photo5 = profile_data.get('photo5', profile.photo5)
        profile.photo6 = profile_data.get('photo6', profile.photo6)
        profile.specializations = profile_data.get(
            'specializations', profile.specializations)
        profile.save()
        return instance





