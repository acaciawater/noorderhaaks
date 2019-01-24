'''
Created on Jan 2, 2019

@author: theo
'''
from acacia.data.views import ProjectDetailView
from acacia.data.models import Project
import json
from django.template.loader import render_to_string
from django.conf import settings
from django.views.generic.detail import DetailView

class HomeView(DetailView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        project = self.get_object()
        content = []
        for ploc in project.projectlocatie_set.all():
            for loc in ploc.meetlocatie_set.all():
                pos = loc.latlon()
                content.append({
                                'id': loc.id,
                                'name': loc.name,
                                'lat': pos.y,
                                'lon': pos.x,
                                'info': render_to_string('data/meetlocatie_info.html', {'object': loc})
                                })
        context['content'] = json.dumps(content)
        context['apikey'] = settings.GOOGLE_MAPS_API_KEY
        context['maptype'] = 'SATELLITE'
        context['zoom'] = 14
        return context
    
    def get_object(self, queryset=None):
        return Project.objects.first()
