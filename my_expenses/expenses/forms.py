from django.forms import ModelForm
from django.forms import Form
from django import forms
from expenses.models import Expense
from expenses.models import ExpenseCategory


class ExpenseCreateForm(ModelForm):

    class Meta:
        model = Expense
        fields = ['name', 'price', 'bought_at', 'category']


class CategoryCreateForm(ModelForm):

    class Meta:
        model = ExpenseCategory
        fields = ['name']


class ExpenseChoiceForm(Form):
    YEAR_CHOICES = [(year, str(year)) for year in range(1990, 2030)]
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    MONTH_CHOICES = [(0, 'cały rok')] + [(month, str(month)) for month in range(1, 13)]
    month = forms.ChoiceField(choices=MONTH_CHOICES)
