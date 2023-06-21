from rest_framework import serializers
from auth.serializers import (UserSerializer)

class SupplyChainBaseSerializer(serializers.ModelSerializer):
    created_by =  serializers.PrimaryKeyRelatedField(default=UserSerializer(), read_only=True)

    class Meta:
        fields = '__all__'
        # exclude = ['created_by', 'created_at']
        read_only_fields = ['created_at','updated_at']

    
    def validate(self, attrs):
        # attrs.created_by = User()
        attrs['created_by_id'] = self.context['request'].user
        return super().validate(attrs)


 
