from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets , permissions


class CityViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows to add or modify cities by
        the admin
        this endpoint allows  GET,POST,PUT,PATCH,DELETE function
        permissions to this view is restricted as the following:
        - only admin users can access this api
         Data will be retrieved in the following format using GET function:
       {
        "id": 26,
        "name": "city_name",
        "state": state_id,
       }
      Use PUT function by accessing this url:
      /address/modifyCity/<city's_id>
      Format of data will be as the previous data format for GET function

      """
    from address.serializers import CitySerializer
    # set view Name as "Create/Modify Cities' Data"
    def get_view_name(self):
        return _("Create/Modify Cities' Data")

    from address.models import City
    # get all Cities from DB
    queryset = City.objects.all()
    # Specifying serializer class
    serializer_class = CitySerializer
    # set permission for Admin users only
    permission_classes = [permissions.IsAdminUser]


class CountryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows to add or modify countries by
        the admin
        this endpoint allows  GET,POST,PUT,PATCH,DELETE function
        permissions to this view is restricted as the following:
        - only admin users can access this api
         Data will be retrieved in the following format using GET function:
       {
        "id": 26,
        "name": "country_name",

       }
      Use PUT function by accessing this url:
      /address/modifyCountry/<country's_id>
      Format of data will be as the previous data format for GET function

      """
    from address.serializers import CountrySerializer
    # set view name as "Create/Modify Countries' Data"
    def get_view_name(self):
        return _("Create/Modify Countries' Data")

    from address.models import Country
    # get all Countries in DB
    queryset = Country.objects.all()
    # Specifying serializer class
    serializer_class = CountrySerializer
    # set permission to Admin users only
    permission_classes = [permissions.IsAdminUser]


class StateViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows to add or modify states by
        the admin
        this endpoint allows  GET,POST,PUT,PATCH,DELETE function
        permissions to this view is restricted as the following:
        - only admin users can access this api
         Data will be retrieved in the following format using GET function:
       {
        "id": 26,
        "name": "country_name",
        "country": country_id,

       }
      Use PUT function by accessing this url:
      /address/modifyState/<country's_id>
      Format of data will be as the previous data format for GET function

      """
    from address.serializers import StateSerializer
    # set view name as "Create/Modify States' Data"
    def get_view_name(self):
        return _("Create/Modify States' Data")

    from address.models import State
    # get all states from DB
    queryset = State.objects.all()
    # Specifying serializer class
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAdminUser]


