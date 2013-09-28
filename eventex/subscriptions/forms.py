# coding: utf-8
from django import forms
from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
	name = forms.CharField(error_messages={'required': 'Preencha o nome de cadastro.'})
	cpf = forms.CharField(error_messages={'required': 'Preencha um CPF único.'})
	email = forms.CharField(error_messages={'required': 'Preencha um e-mail para contato.'})
	class Meta:
		model = Subscription