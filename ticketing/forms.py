from django import forms
from ticketing.models import Cinema

class ShowTimeSearchForm(forms.Form):
    PRICE_ANY = '0'
    PRICE_UNDER_10 = '1'
    PRICE_10_TO_15 = '2'
    PRICE_15_TO_20 = '3'
    PRICE_ABOVE_20 = '4'
    PRICE_LEVEL_CHOICES = (
        (PRICE_ANY, 'any price'),
        (PRICE_UNDER_10, 'up to 10T'),
        (PRICE_10_TO_15, '10T to 15T'),
        (PRICE_15_TO_20, '15T to 20T'),
        (PRICE_ABOVE_20, 'more than 20T'),
    )

    movie_name = forms.CharField(max_length=100, required=False)
    sale_is_open = forms.BooleanField(required=False)
    movie_length_min = forms.IntegerField(min_value=0, max_value=200, required=False)
    movie_length_max = forms.IntegerField(min_value=0, max_value=200, required=False)
    cinema = forms.ModelChoiceField(required=False, queryset=Cinema.objects.all())
    price_level = forms.ChoiceField(choices=PRICE_LEVEL_CHOICES, required=False)

    def get_price_boundries(self):
        price_level = self.cleaned_data['price_level']
        if price_level == ShowTimeSearchForm.PRICE_UNDER_10:
            return None, 10000
        elif price_level == ShowTimeSearchForm.PRICE_10_TO_15:
            return 10000, 15000
        elif price_level == ShowTimeSearchForm.PRICE_15_TO_20:
            return 15000, 20000
        elif price_level == ShowTimeSearchForm.PRICE_ABOVE_20:
            return 20000, None
        else:
            return None, None