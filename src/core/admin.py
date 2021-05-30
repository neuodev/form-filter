from django.contrib import admin


from .models import Author,Category,Journal


class JournalAdmin(admin.ModelAdmin):
    list_display=('title','publish_date','reviewed')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Journal ,JournalAdmin)