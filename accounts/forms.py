from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError

from accounts.models import Payment, Profile


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'transaction_code']

    def clean_transaction_code(self):
        code = self.cleaned_data.get('transaction_code')
        try:
            # should be in format: bank-<amount>-<TOKEN>#
            assert code.startswith('bank-')
            assert code.endswith('#')
            int(code.split('-')[1])
        except:
            raise ValidationError('Receipt is not valid')
        return code


    def clean(self):
        super().clean()
        code = self.cleaned_data.get('transaction_code')
        amount = self.cleaned_data.get('amount')
        if code and amount:
            if int(code.split('-')[1]) != amount:
                raise ValidationError('Receipt and deposit value do not match')


