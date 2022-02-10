from django.contrib import admin
from .models import Place
from .models import Tour_package
from .models import Team
# Register your models here.
admin.site.register(Place)
admin.site.register(Tour_package)
admin.site.register(Team)