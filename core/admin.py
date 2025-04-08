from django.contrib import admin
from .models import Contact, News, NewsCategory, Advertisement, Subscribe


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'featured_type')  # Featured sahəsini əlavə
    search_fields = ('title', 'content')  # Axtarış funksiyası əlavə etmək
    list_filter = ('categories', 'featured_type')


    # Categories sahəsi
    filter_horizontal = ('categories',)

# NewsCategory modelini admin panelində göstərmək
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Kateqoriya adını göstərmək

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'columns')

# Modelləri admin panelinə qeydiyyatdan keçirmək
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contact)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Subscribe)
