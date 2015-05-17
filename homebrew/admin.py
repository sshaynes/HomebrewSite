from django.contrib import admin
from homebrew.models import Hop, Grain, Yeast, Profile, Recipe

class UserProfileAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['user']}),
    (None,               {'fields': ['age']}),
    (None,               {'fields': ['location']}),
    (None,               {'fields': ['yearsExperience']}),
    (None,               {'fields': ['avatarURL']}),
    (None,               {'fields': ['reg_date']}),
    (None,               {'fields': ['update_date']}),
  ]
  list_display = ('user', 'yearsExperience', 'reg_date')
  list_filter = ['user']
  search_fields = ['user']


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
class YeastAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		(None,               {'fields': ['type']}),
		(None,               {'fields': ['form']}),
		(None,               {'fields': ['laboratory']}),
		(None,               {'fields': ['amount']}),
		(None,               {'fields': ['amount_is_weight']}),
		(None,               {'fields': ['product_id']}),
		(None,               {'fields': ['min_temperature']}),
		(None,               {'fields': ['max_temperature']}),
		(None,               {'fields': ['flocculation']}),
		(None,               {'fields': ['attenuation']}),
		(None,               {'fields': ['notes']}),
		(None,               {'fields': ['best_for']}),
		(None,               {'fields': ['times_cultured']}),
		(None,               {'fields': ['max_reuse']}),
		(None,               {'fields': ['add_to_secondary']}),
		(None,               {'fields': ['display_amount']}),
		(None,               {'fields': ['disp_min_temp']}),
		(None,               {'fields': ['disp_max_temp']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'pub_date', 'notes')
	list_filter = ['pub_date']
	search_fields = ['name']
class RecipeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['userid']}),
		(None,               {'fields': ['styleid']}),
		(None,               {'fields': ['substyleid']}),
		(None,               {'fields': ['description']}),
		(None,               {'fields': ['boilTime']}),
		(None,               {'fields': ['method']}),
		(None,               {'fields': ['batchSize']}),
		(None,               {'fields': ['boilSize']}),
		(None,               {'fields': ['ibu']}),
		(None,               {'fields': ['abv']}),
		(None,               {'fields': ['name']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'styleid', 'substyleid')
	list_filter = ['pub_date']
	search_fields = ['name']

admin.site.register(Hop, HopAdmin)
admin.site.register(Grain, GrainAdmin)
admin.site.register(Yeast, YeastAdmin)
admin.site.register(Profile, UserProfileAdmin)
admin.site.register(Recipe, RecipeAdmin)