from django.contrib import admin

from app.models.card_info import WarningCardInfo, SolveCardInfo
from app.models.volunteer import VolunList

admin.site.register(WarningCardInfo)
admin.site.register(SolveCardInfo)
admin.site.register(VolunList)
