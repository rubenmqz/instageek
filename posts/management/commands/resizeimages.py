from django.core.management import BaseCommand

from posts.models import Post
from posts.utils import generate_responsive_images


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Fetching posts to resize its images")
        posts = Post.objects.filter(image_resized=False)
        self.stdout.write("{0} posts to resize its images".format(posts.count()))
        for possible_post in posts:
            try:
                post = Post.objects.get(pk=possible_post.pk, image_resized=False)
                self.stdout.write("Resizing posts {0} image".format(post.pk))
                generate_responsive_images(post)
                self.stdout.write(self.style.SUCCESS("Post {0}'s image resized successfully!".format(post.pk)))
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR("Post {0}'s image already resized".format(post.pk)))


