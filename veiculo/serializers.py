from rest_framework import serializers
from veiculo.models import Veiculo
from drf_extra_fields.fields import Base64ImageField

class SerializadorVeiculo(serializers.ModelSerializer):
    """
    Serializador para modelo de veiculo
    """
    nome_marca = serializers.SerializerMethodField()
    nome_cor = serializers.SerializerMethodField()
    nome_combustivel = serializers.SerializerMethodField()
    foto = Base64ImageField(required=False, represent_in_base64=True)

    class Meta:
        model = Veiculo
        exclude = []

    def get_nome_marca(self, instancia):
        return instancia.get_marca_display()

    def get_nome_cor(self, instancia):
        return instancia.get_cor_display()

    def get_nome_combustivel(self, instancia):
        return instancia.get_combustivel_display()