from django.shortcuts import redirect, render
from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'account/register.html', context)

