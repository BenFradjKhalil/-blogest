
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

from articles.forms import ArticlesForm
from .models import Articles
from django.shortcuts import get_object_or_404



def articles_view(request):
    articles=Articles.objects.all().order_by('-date_publication')
    return render(request,'articles/articles.html', context={'articles': articles})

def article_view(request, slug):  
    try :
        article=Articles.objects.get(slug=slug)
        return render(request,'articles/detail.html', context={'article': article})
    except Articles.DoesNotExist:
        raise Http404("L'article n'existe pas" )
    #article=get_object_or_404(Articles,slug=slug)
    #return render(request,'articles/detail.html', context={'article': article})
   

def creer_view(request):
    form=ArticlesForm
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('articles:articles'))
        
    return render(request,'articles/creer.html' , context={'form':form})

