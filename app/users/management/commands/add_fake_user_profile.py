from django.core.management.base import BaseCommand
from django.utils.text import slugify
import uuid
from faker import Faker
from users.models import Profile, User


class Command(BaseCommand):
    help = 'Updates or creates profiles for each existing user.'

    def handle(self, *args, **options):
        fake = Faker()
        users = User.objects.all()

        for user in users:
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'post': fake.job(),
                    'gender': fake.random_element(elements=('F', 'M')),
                    'phone': fake.phone_number(),
                }
            )

            if not created:
                # If the profile already exists, you can update it with new fake data
                profile.first_name = fake.first_name()
                profile.last_name = fake.last_name()
                profile.post = fake.job()
                profile.gender = fake.random_element(elements=('F', 'M'))
                profile.phone = fake.phone_number()
                # Save the updated profile
                profile.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully {"created" if created else "updated"} profile for "{user.username}"'))

