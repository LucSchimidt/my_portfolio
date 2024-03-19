from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView



class HomePageView(TemplateView):
	
	template_name = 'home.html'


class TechPageView(TemplateView):
	
	template_name = 'tech.html'


class ArchivePageView(TemplateView):
	
	template_name = 'archive.html'