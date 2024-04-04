from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates specified number of fake users.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake users to create.')

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()

        created_count = 0

        for _ in range(count):
            try:
                # Generate unique username
                while True:
                    username = fake.user_name()
                    if not User.objects.filter(username=username).exists():
                        break

                user = User.objects.create_user(
                    username=username,
                    email=fake.email(),
                    password='password'  # Consider using a more secure default password
                )

                # Random assignment of roles
                user.is_clerk = random.choice([True, False])
                user.is_manager = not user.is_clerk  # Or any logic you prefer
                user.save()

                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to create user: {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} users.'))
