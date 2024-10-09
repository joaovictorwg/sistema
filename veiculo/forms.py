from django.forms import ModelForm
from veiculo.models import Veiculo

class FormularioVeiculo(ModelForm):
    # Formulario para o model veiculo
    class Meta:
        model = Veiculo
        exclude = []