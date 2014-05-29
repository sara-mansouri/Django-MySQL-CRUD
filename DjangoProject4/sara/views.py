# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from django.http import HttpResponse
from django.shortcuts import render
from sara.models import Person


def ss(request):
    if request.method == 'GET':
        output=Person.objects.all()
        context = {'content': output}
        return render(request, 'index.html', context)
    if request.method == 'POST' and 'submitwhat' in request.POST:
        fard = Person()
        fard.name = request.POST['name']
        fard.email = request.POST['email']
        fard.save()
        
        output=Person.objects.all()
        
        temp={'content':output,}
        return render(request, 'index.html', temp)
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
        retwhat = request.POST["retwhat"]
        fard = Person.objects.get(id = int(retwhat))
        
 
        temp = {
            'aaa_id':retwhat,
            'aaa_name': fard.name,
            'aaa_email': fard.email,
            'VIS':'visibile',
            'VIS1':'hidden',
        }
        return render(request, 'index.html', temp)

    if request.method=='POST' and 'edwhat' in request.POST:
        edwhat=request.POST['edwhat']
        fard = Person.objects.get(id = int(edwhat))

        
        fard.name = request.POST['name']
        fard.email = request.POST['email']
        fard.save()
        
        output=Person.objects.all()
        
        temp={'content':output,}
        return render(request, 'index.html', temp)
        
        output=Person.objects.all()
        template= loader.get_template('index.html')
        context=RequestContext(request,{'content':output,})
        return HttpResponse(template.render(context))