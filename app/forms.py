from django import forms
from .models import registro, destino
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class registroForm(forms.ModelForm):

    class Meta:
        model = registro
        #fields = ["nombre", "correo", "nacionalidad","tipo_consulta","mensaje"]
        fields = '__all__'

class destinoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    pais = forms.CharField(min_length= 5, max_length= 50)
    ciudad = forms.CharField(min_length= 5, max_length= 50)
    tipo = forms.CharField(min_length= 5, max_length= 50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])


    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = destino.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise  ValidationError("Este destino ya esta registrado")  

        return nombre    

    class Meta:
        model = destino
        fields = '__all__'        

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
  