from django.forms import EmailInput, ModelForm
from personapp.models import Person

class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),
        }