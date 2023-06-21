from rest_framework import serializers
from .models import SupplyChainItem
from auth.serializers import (UserSerializer)

class SupplyChainItemSerializer(serializers.ModelSerializer):
    created_by =  serializers.PrimaryKeyRelatedField(default=UserSerializer(), read_only=True)
    # created_by =  UserSerialize(requi))

    class Meta:
        model = SupplyChainItem
        fields = '__all__'
        # exclude = ['created_by', 'created_at']
        read_only_fields = ['created_at','updated_at']

    
    def validate(self, attrs):
        # attrs.created_by = User()
        attrs['created_by_id'] = self.context['request'].user
        return super().validate(attrs)
    
    def save(self, **kwargs):
        # if creating record.
        return super().save(**kwargs)

 
