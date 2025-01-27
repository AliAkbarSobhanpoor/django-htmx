from django.core.management.base import BaseCommand
from htmx.models import Blog
from django.contrib.auth import get_user_model
from faker import Faker

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
                Blog(
                    user=user,
                    title=fake.sentence(),
                    content=fake.paragraph(nb_sentences=5),
                )
            )

        Blog.objects.bulk_create(blogs)
        self.stdout.write(self.style.SUCCESS("100 blog posts added successfully!"))
