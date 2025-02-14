from rest_framework import serializers

from api.models import Lead

# rest_framework/ serializers.py/ class Serializer or class ModelSerializer
# we need to create and update model so, we use ModelSerializer.


class LeadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lead

        fields = "__all__"

        read_only_fields = ["id", "created_date", "updated_at"]  # This variable name is unchangeble. These data are ignored while filling the data by the enduser.




















        