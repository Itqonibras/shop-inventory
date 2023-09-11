from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rose Gold',
        'description': 'Low HP shield',
        'amount': '2',
    }

    return render(request, "main.html", context)