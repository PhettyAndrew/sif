from django.contrib import admin
from . models import Management, Team, News, Donations, Support, GeneralInfo, ShowImages

# Register your models here.
admin.site.register(Management)
admin.site.register(Team)
admin.site.register(News)
admin.site.register(Donations)
admin.site.register(Support)
admin.site.register(GeneralInfo)
admin.site.register(ShowImages)

