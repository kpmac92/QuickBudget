from django.shortcuts import render
from django.http import HttpResponse

from .models import BudgetCategory


# Create your views here.
def index(request):
    return render(request, 'quickBudget/index.html')


def budget(request):
    categories_list = BudgetCategory.objects.order_by('-id')
    context = {
        'categories_list': categories_list,
    }
    return render(request, 'quickBudget/budget.html', context)

