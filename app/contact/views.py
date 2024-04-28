from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
# from .models import ContactInfo
from .forms import AppealingForm


def contact(request):
    # contact_info = ContactInfo.objects.first()
    form = AppealingForm()

    if request.method == 'POST':
        form = AppealingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message is sent successfully!'))
            return redirect('contact')
        
    context = {
        # 'contact_info': contact_info,
        'form': form
    }

    return render(request, 'contact/index.html', context)