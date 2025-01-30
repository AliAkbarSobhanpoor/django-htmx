from django.core.management.base import BaseCommand
from blog.models import Post
from django.contrib.auth import get_user_model
from faker import Faker
import random

class Command(BaseCommand):
    help = "Add 100 blog posts to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        user = get_user_model().objects.first()  # Replace with logic to select a specific user if needed

        if not user:
            self.stdout.write(self.style.ERROR("No user found in the database."))
            return

        blogs = []
        for i in range(100):
            blogs.append(
                Post(
                    title=fake.sentence(),
                    context=fake.paragraph(nb_sentences=5),
                    ia_archived=bool(random.randint(0,1))
                )
            )

        Post.objects.bulk_create(blogs)
        self.stdout.write(self.style.SUCCESS("100 blog posts added successfully!"))
