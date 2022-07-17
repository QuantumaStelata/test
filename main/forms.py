from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

from .models import Term, Brand, Style

class MainForm(forms.Form):
    term = forms.ModelChoiceField(queryset=Term.objects.none())
    brand = forms.ModelChoiceField(queryset=Brand.objects.none(), required=False)
    style = forms.ModelChoiceField(queryset=Style.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    'term',
                    css_class='col-6 mt-2'
                )
            ),
            Row(
                Column(
                    'brand',
                    css_class='col-6 mt-2'
                )
            ),
            Row(
                Column(
                    'style',
                    css_class='col-6 mt-2'
                )
            ),
            Row(
                Column(
                    Submit('search', 'Search', css_class='btn-sm'),
                    css_class='col-6 mt-3'
                )
            )
        )
