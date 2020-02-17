from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import *
from decimal import Decimal
from rest_framework.response import Response

class AccSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model=Acc
        fields='__all__'

class CustomerReferenceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model=Customer
        fields=('id',)

class SubscriberReferenceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model=Subscriber
        fields=('id',)
        
class RecargaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    beneficiary = CustomerReferenceSerializer(read_only=False,many=False)

    def create(self, validated_data):
        beneficiary = validated_data.pop('beneficiary')
        amount = validated_data.pop('amount')
        try:
            myBeneficiary = Customer.objects.get(id=beneficiary['id'])  
            print("encontrado")
        except:
            print("not found")
            raise Exception('Quien eres')
        myBeneficiary.balance=myBeneficiary.balance + amount
        myBeneficiary.save()
        recarga = Recarga.objects.create(beneficiary=myBeneficiary,amount=amount,**validated_data)
        return recarga

    class Meta:
        model=Recarga
        fields='__all__'

class ApiUsageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    consumer = CustomerReferenceSerializer(read_only=False,many=False)

    def create(self, validated_data):

        serviceProvided = validated_data.pop('serviceProvided')
        consumer = validated_data.pop('consumer')
        try:
            myConsumer = Subscribers.objects.get(id=consumer['id'])
            print("found")
        except:
            print("not found")
            raise Exception('Quien eres')
        
        if serviceProvided=="GENVZ":
            myConsumer.balance=myConsumer.balance - Decimal('0.001')
        myConsumer.save()
        apiUsage = ApiUsage.objects.create(consumer=myConsumer,serviceProvided=serviceProvided)
        return apiUsage

    class Meta:
        model=ApiUsage
        fields='__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model=Subscriber
        fields=('id','username',)

class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    apiUsageHistory=ApiUsageSerializer(read_only=True,many=True)
    recargasHistory=RecargaSerializer(read_only=True,many=True)
    usergaHistory=AccSerializer(read_only=True,many=True)
    subscribers=SubscriberSerializer(read_only=True,many=True)
    class Meta:
        model=Customer
        fields='__all__'

class CustomerWithTokenSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)
        return token
    
    class Meta:
        model = Customer
        fields = ('token', 'username', 'password', 'first_name',
        'last_name')