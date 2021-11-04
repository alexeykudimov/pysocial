from django.core.management.base import BaseCommand
from src.profiles.models import SocUser as User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            print('Creating superuser...')
            admin = User.objects.create_superuser(
                email='su@pysocial.net',
                username='su',
                password='4321'
            )
            admin.is_active = True
            admin.save()
        else:
            print('Superuser exists.')