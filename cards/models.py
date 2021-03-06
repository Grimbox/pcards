﻿#coding=utf-8

from django.db import models

class Country(models.Model):
	label = models.CharField(verbose_name='Pays', unique=True, max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural ='Pays'
		verbose_name = 'Pays'
		ordering = ['label']
		
	def __str__(self):
		return self.label
		
	def __unicode__(self):
		return self.label
		
class Category(models.Model):
	label = models.CharField(verbose_name='Catégorie', unique=True,  max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural ='Catégories'
		verbose_name = 'Catégorie'
		ordering = ['label']
		
	def __unicode__(self):
		return self.label

class SubCategory(models.Model):
	label = models.CharField(verbose_name='Thème', unique=True, max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, verbose_name='Catégorie', null=True, blank=True)
	
	class Meta:
		verbose_name_plural ='Thèmes'
		verbose_name = 'Thème'
		ordering = ['label']
		
	def __unicode__(self):
		return self.label

class Tag(models.Model):
	label = models.CharField(verbose_name='Label', unique=True, max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural = 'Tags'
		verbose_name = 'Tag'
		ordering = ['label']
	
	def __unicode__(self):
		return self.label


class Card(models.Model):
	country = models.ForeignKey(Country, verbose_name='Pays')
	label = models.CharField(verbose_name='Titre', max_length=255)
	image = models.ImageField(upload_to='pictures')
	with_chip = models.BooleanField(verbose_name='Avec ou sans puce', blank=True)
	units = models.CharField(verbose_name="Nombre d'unités", max_length=50, blank=True)
	emissionDate = models.CharField(verbose_name="Année ou date d'émission", max_length=10, blank=True)
	expirationDate = models.CharField(verbose_name="Année ou date d'expiration", max_length=10, blank=True)
	numberOfCopies = models.CharField(verbose_name='Tirage', max_length=50, blank=True)
	tags = models.ManyToManyField(Tag, null=True, blank=True, verbose_name='Liste des tags', related_name='tags')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)	
	
	class Meta:
		verbose_name_plural ='Cartes de téléphone'
		verbose_name = 'Carte de téléphone'
	
	def __unicode__(self):
		return '%s %s' % (self.country.label, self.label)
		

