from django.contrib import admin
from django.utils.html import format_html
from .models import *
from .models import Article
from .models import ExperimentoVideo
from .models import Biography
from .models import Revista
from .models import Noticia
from .models import Biografia
from .models import Novidade

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
admin.site.register(Article, ArticleAdmin)

class ExperimentoVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
admin.site.register(ExperimentoVideo, ExperimentoVideoAdmin)

@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death')
    search_fields = ('name',)

class RevistaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo',)
admin.site.register(Revista, RevistaAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'link_externo')

    def link_externo(self, obj):
        if obj.link:
            return format_html('<a href="{}" target="_blank">Abrir link</a>', obj.link)
        return "Sem link"
admin.site.register(Noticia, NoticiaAdmin)

class BiografiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'data_falecimento')
    search_fields = ('nome',)
    list_filter = ('data_nascimento', 'data_falecimento')
    fieldsets = (
        ('Informações Pessoais', {'fields': ('nome', 'data_nascimento', 'data_falecimento')}),
        ('Conteúdo da Biografia', {'fields': ('imagem', 'descricao')}),
    )
    readonly_fields = ()
admin.site.register(Biografia, BiografiaAdmin)

class NovidadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data_publicacao',)
    ordering = ('-data_publicacao',)
admin.site.register(Novidade, NovidadeAdmin)