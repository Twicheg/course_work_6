from django import forms

from newsletter.models import MessageSettings, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MessageSettings
        fields = '__all__'


class MessageCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        # fields = '__all__'
        exclude = ('client',)
