from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


# this class is responsible to make the serialization processing for User model data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        from accounts.models import User
        # choosing "User Model" to serialize its objects
        model = User
        # fields that will be available in the API endpoint later
        fields = (
            'id', 'full_name', 'is_customer',
                                          'email','city','street_address', 'phone_number', 'password')


# this class is responsible for providing an endpoint
# allows the user to change their passwords in case if they forget it
class ForgetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, validators=[validate_password], label=_('New Password'))
    password2 = serializers.CharField(write_only=True, required=True, label=_('Confirm Password'))

    class Meta:
        from accounts.models import User
        model = User
        fields = ('password', 'password2')

    # validate that the two fields of passwords are match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    # update the old password with the new one
    def update(self, instance, validated_data):
        print("setting new password: ", validated_data['password'])
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

# this class is used to register new users using API endpoints
class RegisterSerializer(serializers.ModelSerializer):
    from rest_framework.validators import UniqueValidator
    from django.core.validators import RegexValidator
    from accounts.models import User
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone_number = serializers.CharField(
        label=_('Phone Number'),
        required=True

    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label=_('Confirm Password'))

    class Meta:
        from accounts.models import User
        model = User
        fields = (
            'id', 'full_name', 'is_customer',
                               'email', 'city', 'street_address', 'phone_number', 'password','password2')


    # validate that the two password fields are match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    # create new user record
    def create(self, validated_data):
        from accounts.models import User
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    # update user data
    def update(self, instance, validated_data):
        instance.phone_number = validated_data['phone_number']
        instance.full_name = validated_data['full_name']
        instance.email = validated_data['email']
        instance.set_password(validated_data['password'])
        instance.address = validated_data['address']
        instance.save()
        return instance
