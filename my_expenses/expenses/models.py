from django.db import models


class Expense(models.Model):
    '''
    piszemy nazwę klasy ExpenseCategory w "", bo klasa występuje poniżej.
    Robimy stringa i będzie ok.
    https://docs.djangoproject.com/en/2.1/ref/models/fields/#foreignkey
    '''
    category = models.ForeignKey("ExpenseCategory", on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bought_at = models.DateTimeField()

    def __str__(self):
        return self.name


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




