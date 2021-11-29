from rest_framework import serializers


# this class is responsible for making the serialization processing for Country model data
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Country
        # choosing the "Country" model
        model = Country
        # choosing all fields of the "Country" model except "slug" field
        exclude = ('slug',)


# this class is responsible for making the serialization processing for State model data
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import State
        # choosing the "State" model
        model = State
        # choosing all fields of the "State" model except "slug" field
        exclude = ('slug',)


# this class is responsible for making the serialization processing for City model data
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import City
        # choosing the "City" model
        model = City
        # choosing all fields "City" model except "slug" field
        exclude = ('slug',)
