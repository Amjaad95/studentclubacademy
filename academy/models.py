# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cours(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instruction = models.ManyToManyField(Instruction)
    graduates = models.ManyToManyField(Graduates)
    session_count = models.IntegerField
    homeworks_count = models.IntegerField
    batch_count = models.IntegerField

class Instructor(models.Model):
    user =
    experience = models.TextField(blank=True)
    email =
    twitter_account = models.CharField(max_length=200)

class Graduates(models.Model):
    user =
    email =
    batch = models.IntegerField
    college = graduate.user.profile.collage
    course = models.ManyToManyField(Cours)
    twitter_account = models.CharField(max_length=200)
    Telegram_account = models.CharField(max_length=200)
    experience = models.TextField(blank=True)

class Work(models.Model):
    graduate = models.ManyToManyField(Graduate)
    short_Descruption = models.CharField(max_length=200)
    Long_descruption =  models.TextField(blank=True)
    Projects_in_studentclub = models.TextField(blank=True)
    Projects_outside_studentclub = models.TextField(blank=True)
    done_projects = models.FileField(upload_to="academy_done_projects", blank=True)

class NewStudent(models.Model):
    user =
    batch = models.IntegerField
    worked_in_stuedntclub = models.TextField
    past_Experience = models.TextField
    why_would_you_join_us = models.TextField
    wants_to_work = models.BooleanField(default=False)
