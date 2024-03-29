from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models



class HomePageView(TemplateView):
	
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['ultimos_trabalhos'] = models.Item.objects.filter(type=0).order_by('created_at')[:4]
		context['ultimos_blogs'] = models.Item.objects.filter(type=1).order_by('created_at')[:4]
		return context


class TechPageView(TemplateView):
	
	template_name = 'tech.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tech'] = models.Tech.objects.all()
		return context


class ArchivePageView(TemplateView):
	
	template_name = 'archive.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['arquivo'] = models.Item.objects.all().order_by('-created_at')
		return context


class PopUpPage(DetailView):
	template_name = 'item_detail.html'
	model = models.Item
	