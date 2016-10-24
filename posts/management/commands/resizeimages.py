from django.core.management import BaseCommand

from posts.models import Post
from posts.utils import generate_responsive_images


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Fetching posts to resize its images")
        posts = Post.objects.filter(image_resized=False)
        self.stdout.write("{0} posts to resize its images".format(posts.count()))
        for post in posts:
            self.stdout.write('Resizing post {0} image'.format(post.pk))
            generate_responsive_images(post)
            post.image_resized = True
            post.save()
            self.stdout.write(self.style.SUCCESS('Post {0} image resized successfully'.format(post.pk)))


