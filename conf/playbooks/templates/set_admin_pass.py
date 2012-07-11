import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mango.settings")

from django.contrib.auth.models import User


admin = User.objects.get(id=1)
admin.set_password("{{ admin_password }}")
admin.save()
