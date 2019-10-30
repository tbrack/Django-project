from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class BlogFeed(Feed):
    title = "My Blog Feed"
    link = "/latest/feed"
    description = "RSS feed of blog posts"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_text(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
