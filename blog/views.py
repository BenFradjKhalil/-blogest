
from django.shortcuts import render
from django.urls.base import reverse

from articles.forms import ArticlesForm
from .forms import ContactForm
from django.http import HttpResponse , HttpResponseRedirect
from django.core.mail import send_mail
def home_view(request):
    return render(request,'home.html')


def contact_view(request):
    form=ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid() :
            nom=form.cleaned_data['nom']
            prenom=form.cleaned_data['prenom']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            titre=f'blog | {nom} {prenom} - {email} '
            send_mail(titre ,message , 'benfradjkhalil111@gmail.com' , ['khalil.benfradj11@gmail.com'])
        return HttpResponseRedirect(reverse('remerciements'))
    return render(request,'contact.html',{'form':form})

def remerciements_view (request):
    return HttpResponse('Merci de nous contacté')