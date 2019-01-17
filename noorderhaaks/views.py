'''
Created on Jan 2, 2019

@author: theo
'''
from acacia.data.views import ProjectDetailView
from acacia.data.models import Project

class HomeView(ProjectDetailView):
    def get_context_data(self, **kwargs):
        context = ProjectDetailView.get_context_data(self, **kwargs)
        context['maptype'] = 'SATELLITE'
        context['zoom'] = 14
        return context
    
    def get_object(self, queryset=None):
        return Project.objects.first()
