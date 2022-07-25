from django.db import models
from django.views.generic import ListView, DetailView
from django.core.exceptions import BadRequest, PermissionDenied
from .models import Article, Section, Status
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(LoginRequiredMixin, ListView):
    template_name="article/list.html"
    model= Article
    

    def set_sections(self, context): 
        context["sections"]=Section.objects.all()

    def set_status(self, context):
        context["satuses"] = Status.objects.all()

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        status_id = self.kwargs.get("status")
        section_id=self.kwargs.get("section")
        status = Status.objects.get(id=kwargs.get("status"))
        section= Section.objects.get(id=kwargs.get("section"))
        if status.id == 1:
            context["article_list"]= Article.objects.filter(
                section=section
            ).order_by("created_on").reverse()
            return context
        if self.request.user.role.id > 1:
         context["article_list"]=Article.objects.filter(status=status).filter(
            section=section
         ).order_by("created_on").reverse()
         return context
        raise PermissionDenied ("You are not authorized on this page")
        
        
  