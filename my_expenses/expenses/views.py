from django.shortcuts import render, redirect
from expenses.forms import ExpenseCreateForm
from expenses.forms import CategoryCreateForm
from expenses.forms import ExpenseChoiceForm
from django.views.decorators.http import require_http_methods
from expenses.models import Expense
from expenses.models import ExpenseCategory


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == 'POST':
        expense_create_form = ExpenseCreateForm(request.POST)
        if expense_create_form.is_valid():
            expense_create_form.save()
            return redirect('/')
    else:
        expense_create_form = ExpenseCreateForm()
    all_expenses = Expense.objects.all()
    expense_choice_form = ExpenseChoiceForm(request.GET)
    if expense_choice_form.is_valid():
        all_expenses = all_expenses.filter(bought_at__year=expense_choice_form.cleaned_data['year'])
        if expense_choice_form.cleaned_data['month'] != '0':
            print(expense_choice_form.cleaned_data)
            all_expenses = all_expenses.filter(bought_at__month = expense_choice_form.cleaned_data['month'])
    sum_of_expences = 0
    for expense in all_expenses:
        sum_of_expences += expense.price
    return render(request, "expenses/home.html", {'expense_create_form': expense_create_form,
                                                  'all_expenses': all_expenses,
                                                  'expense_choice_form': expense_choice_form,
                                                  'sum_of_expences' : sum_of_expences})


@require_http_methods(["GET", "POST"])
def categories(request):
    if request.method == 'POST':
        category_create_form = CategoryCreateForm(request.POST)
        if category_create_form.is_valid():
            category_create_form.save()
            return redirect('/category')
    else:
        category_create_form = CategoryCreateForm()
    all_categories = ExpenseCategory.objects.all()

    return render(request, "expenses/category.html", {'category_create_form': category_create_form,
                                                      'all_categories': all_categories})




