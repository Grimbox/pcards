#coding=utf-8

from django.db import models

class Country(models.Model):
	name = models.CharField(verbose_name='Pays', max_length=50)
	
	class Meta:
		verbose_name_pluralize='Pays'
		
class Category(models.Model):
	label = models.CharField(verbose_name='Label', max_length=50)
	
	class Meta:
		verbose_name_pluralize='Cat�gories'

class SubCategory(models.Model):
	label = models.CharField(verbose_name='Sous-cat�gorie', max_length=50)
	
	class Meta:
		verbose_name_pluralize='Sous-cat�gories'

class Item(models.Model):
	
	country = models.ForeignKey(Country)
	category = models.ForeignKey(Category)
	subcategory = models.ForeignKey(SubCategory)
	label = models.CharField(verbose_name='Label', max_length=50)
	image = models.ImageField(upload_to='pictures')
	
	
	class Meta:
		verbose_name_pluralize='Items'