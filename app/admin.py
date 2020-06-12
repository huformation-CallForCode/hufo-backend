from django.contrib import admin

from app.models.card_info import WarningCardInfo, SolveCardInfo

admin.site.register(WarningCardInfo)
admin.site.register(SolveCardInfo)