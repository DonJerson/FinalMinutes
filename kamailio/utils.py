from kamailio.serializers import CustomerSerializer

def custom_jwt_response_handler(token, user=None, request=None):
    return {
        'token' : token,
        'user' : CustomerSerializer(user, context={'request' : request}).data
    }