from django.shortcuts import render
from django.http import HttpResponse

from .models import BudgetCategory


# Create your views here.
def index(request):
    return render(request, 'quickBudget/index.html')


def create_budget(request):
    context = {
        'categories_list': get_category_list(),
    }
    return render(request, 'quickBudget/createBudget.html', context)


def submit(request):
    context = {
        'category_amounts': dict(zip(get_category_list(), request.POST.getlist('amount', ['0.00'])))
    }
    print(context)
    return render(request, 'quickBudget/displayBudget.html', context)


def get_category_list():
    return BudgetCategory.objects.order_by('-id')