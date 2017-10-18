# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

class MapImage(models.Model):
	name = models.CharField('Name', max_length=100)
	image = models.ImageField(null=True, blank=True)
	location = models.PointField(blank=False, null=False)

	def __str__(self):
		return self.name
