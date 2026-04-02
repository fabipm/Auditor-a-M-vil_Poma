import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scan.models import Scan
for s in Scan.objects.all():
    print(f"Scan ID {s.id}: Status={s.status}, Progress={s.progress}, Findings={s.findings_set.count()}")
