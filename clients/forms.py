from django import forms

from clients.models import Clients


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientsCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

    # def clean_name(self):
    #     bad_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
    #     clean_data = self.cleaned_data['name']
    #     for i in bad_words:
    #         if i in clean_data:
    #             raise forms.ValidationError('Неприемлимое название продукта')
    #
    #     return clean_data
    #
    # def clean_overview(self):
    #     bad_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
    #     clean_data = self.cleaned_data['overview']
    #     for i in bad_words:
    #         if i in clean_data:
    #             raise forms.ValidationError('Неприемлимое описание продукта')
    #
    #     return clean_data
