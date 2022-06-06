
from asyncore import read
from random import random
from assignments.models import assignments 
import random
import string
from rest_framework import serializers
def generate_id():
    random1=""
    random1+= "".join([random.choice(string.ascii_letters + string.digits)
                    for n in range(8)])
    random1+="-"
    random1+= "".join([random.choice(string.ascii_letters + string.digits)
                    for n in range(4)])
    random1+="-"
    random1+= "".join([random.choice(string.ascii_letters + string.digits)
                    for n in range(4)])
    random1+="-"
    random1+= "".join([random.choice(string.ascii_letters + string.digits)
                    for n in range(4)])
    random1+="-"
    random1+= "".join([random.choice(string.ascii_letters + string.digits)
                    for n in range(12)])
    random1 =random1.lower()
    return(random1)

class AssignmentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    email = serializers.EmailField()
    createdAt = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return assignments.objects.create(id=generate_id(),**validated_data)