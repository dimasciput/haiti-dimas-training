# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .models import MapImage
from .forms import MapImageForm

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = 'all_map_image'

	def get_queryset(self):
		return MapImage.objects.all()

class InsertView(FormView):
	template_name = 'map_image_form.html'
	form_class = MapImageForm
	success_url = '/'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed
		post = form.save(commit=False)
		post.name = self.request.POST.get('name')
		post.image = self.request.FILES.get('image')
		post.location = self.request.POST.get('location')
		post.save()
		return super(InsertView, self).form_valid(form)
