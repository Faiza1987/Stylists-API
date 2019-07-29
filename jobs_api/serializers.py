from rest_framework import serializers
from jobs_api.models import Job
from api.models import User


class JobSerializer(serializers.ModelSerializer):

    stylist = serializers.HyperlinkedRelatedField(
        view_name="stylist-detail",
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )

    class Meta:
        model = Job
        fields = ("url", "title", "hourly_rate", "company", "address", "city", "state",
                  "zip_code", "description", "contact_email", "stylist")
