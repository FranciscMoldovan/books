# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    release_date = models.DateField
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)