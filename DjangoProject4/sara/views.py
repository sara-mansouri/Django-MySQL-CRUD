# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader
from sara.models import Person


def ss(request):
    output=Person.objects.all()
    template= loader.get_template('index.html')
    context=RequestContext(request,{'content':output,})

    return HttpResponse(template.render(context))
#class a(webapp2.RequestHandler):
def submitit(self):
         Person.name = self.request.get('name')
         Person.email = self.request.get('email')
         Person.put()

         self.redirect('/?' + urllib.urlencode(query_params))

