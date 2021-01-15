from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import SiteConfig, SiteContent

class UserSerializer(serializers.ModelSerializer):
    site_configs = serializers.PrimaryKeyRelatedField(many=True, queryset=SiteConfig.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'site_configs']

class SiteConfigSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SiteConfig
        fields = ['id', 'site_address', 'articles', 'frequency', 'owner']