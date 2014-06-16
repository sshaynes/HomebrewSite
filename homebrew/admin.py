from django.contrib import admin
from homebrew.models import Hop, Grain

class HopAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		(None,               {'fields': ['origin']}),
		(None,               {'fields': ['time']}),
		(None,               {'fields': ['notes']}),
		(None,               {'fields': ['alpha']}),
		(None,               {'fields': ['amount']}),
		(None,               {'fields': ['use']}),
		(None,               {'fields': ['displayAmount']}),
		(None,               {'fields': ['type']}),
		(None,               {'fields': ['beta']}),
		(None,               {'fields': ['form']}),
		(None,               {'fields': ['displayTime']}),
		(None,               {'fields': ['hsi']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'pub_date', 'notes')
	list_filter = ['pub_date']
	search_fields = ['name']
	
class GrainAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		(None,               {'fields': ['origin']}),
		(None,               {'fields': ['recommendMash']}),
		(None,               {'fields': ['notes']}),
		(None,               {'fields': ['addAfterBoil']}),
		(None,               {'fields': ['amount']}),
		(None,               {'fields': ['maxInBatch']}),
		(None,               {'fields': ['displayAmount']}),
		(None,               {'fields': ['protein']}),
		(None,               {'fields': ['type']}),
		(None,               {'fields': ['supplier']}),
		(None,               {'fields': ['displayColor']}),
		(None,               {'fields': ['potential']}),
		(None,               {'fields': ['moisture']}),
		(None,               {'fields': ['coarseFineDiff']}),
		(None,               {'fields': ['color']}),
		(None,               {'fields': ['extractSubstitue']}),
		(None,               {'fields': ['diastaticPower']}),
		(None,               {'fields': ['ibuGalPerLb']}),
		(None,               {'fields': ['yeild']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'pub_date', 'notes')
	list_filter = ['pub_date']
	search_fields = ['name']

admin.site.register(Hop, HopAdmin)
admin.site.register(Grain, GrainAdmin)