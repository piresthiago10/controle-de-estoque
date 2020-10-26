from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario


class UsuarioSerializer(ModelSerializer):

    senha = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Não preencha caso não haja mudança',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'login', 'senha', 'tipo_usuario')

    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data.get('senha'))
        return super(UsuarioSerializer, self).create(validated_data)
