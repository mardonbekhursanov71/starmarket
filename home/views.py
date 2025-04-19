from django.shortcuts import render, redirect
from .forms import MahsulotForm
from django.views.generic import TemplateView

class Home_Page_Veiw(TemplateView):
    template_name = "index.html"
    

def admin_sahifa(request):
    if request.method == 'POST':
        form = MahsulotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, template_name='succsess.html')
    else:
        form = MahsulotForm()
    return render(request, 'admin.html', {'form': form})