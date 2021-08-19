from django.core.management.base import BaseCommand
from src.profiles.models import SocUser
from src.followers.models import Follower
from src.wall.models import Post
from random import randrange


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_user(10)
        self.create_follower()
        self.create_post(10)

        self.stdout.write('Success')

    def create_user(self, count):
        first_names = [
            "Max",
            "Tim",
            "Alex",
            "Pasha",
            "Misha",
            "Nikita",
            "Grisha",
            "Sergey",
            "Eugene",
            "Vladimir"
        ]
        last_names = [
            "Pavlov",
            "Timurov",
            "Nikitin",
            "Sergeev",
            "Alekseev",
            "Maksimov",
            "Mihailov",
            "Evgeniev",
            "Grigoriev",
            "Vladimirov"
        ]

        for idx in range(count):
            SocUser.objects.create_user(
                username=f"TestUser{idx+1}",
                email=f"tu{idx}@pysocial.net",
                password=f"{randrange(100000000, 999999999)}",
                is_active=True,
                first_name=first_names[randrange(len(first_names))],
                last_name=last_names[randrange(len(last_names))],
                phone='+7900900' + f"{randrange(1000, 9999)}",
                gender=1
            )

    def create_follower(self):
        users = SocUser.objects.order_by()[2:]
        for user in users:
            Follower.objects.create(user=user, follower_id=1)

    def create_post(self, count):
        users = SocUser.objects.all()
        for user in users:
            for idx in range(count):
                Post.objects.create(
                    text=f"Test post {randrange(10000, 99999)}",
                    user=user
                )
