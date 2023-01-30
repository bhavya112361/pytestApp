from rest_framework import serializers
from .models import Client,Projects,Project_Users



class ClientSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Client
        fields=['id','client_name',
                'created_at','updated_at',
                'created_by']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_by'] = instance.created_by.username

        return representation
        

class ProjectsSerializer(serializers.ModelSerializer):
    #created_by = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model=Projects
        fields=['id','client_id','project_name','created_at','created_by']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['client_id']
        representation['created_by'] = instance.created_by.username
        

        return representation

class ProjectUserSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model=Project_Users
        fields=['project_id','User_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['User_id']

        representation['project_name'] = instance.project_id.project_name
        representation['created_at'] = instance.project_id.created_at
        representation['created_by'] = instance.project_id.created_by.username

        return representation
        