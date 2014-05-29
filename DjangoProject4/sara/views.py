# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader
from sara.models import Person


def ss(request):
    if request.method == 'GET':
        output=Person.objects.all()
        template= loader.get_template('index.html')
        context=RequestContext(request,{'content':output,})
        return HttpResponse(template.render(context))
    if request.method == 'POST' and 'submitwhat' in request.POST:
        fard = Person()
        fard.name = request.POST['name']
        fard.email = request.POST['email']
        fard.save()
        
        output=Person.objects.all()
        template= loader.get_template('index.html')
        context=RequestContext(request,{'content':output,})
        return HttpResponse(template.render(context))
      #  return HttpResponse(template.render(context))
      #  return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    
    if request.method=='POST' and 'deletewhat' in request.POST:
        #report = Person.query(Person.id == int(delWhat)).get()
        delWhat = request.POST["deletewhat"]
        fard = Person.objects.filter(id = int(delWhat))
        fard.delete()
        
        output=Person.objects.all()
        template= loader.get_template('index.html')
        context=RequestContext(request,{'content':output,})
        return HttpResponse(template.render(context))

    if request.method=='POST' and 'retwhat' in request.POST:
        fard = Person()
        fard.delete(Person)
        
        output=Person.objects.all()
        template= loader.get_template('index.html')
        context=RequestContext(request,{'content':output,})
        return HttpResponse(template.render(context))

    if request.method=='POST' and 'edittewhat' in request.POST:
        fard = Person()
        fard.delete(Person)
        
        output=Person.objects.all()
        template= loader.get_template('index.html')
        context=RequestContext(request,{'content':output,})
        return HttpResponse(template.render(context))