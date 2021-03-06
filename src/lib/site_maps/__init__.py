from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils import timezone
from lukexor_me import models


class ArticleSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return models.Article.objects.filter(date_published__lte=timezone.now())

    def lastmod(self, item):
        return item.updated

class ArticleTagSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return models.Tag.objects.filter(article__isnull=False).distinct()

    def location(self, item):
        name = slugify(item.name.lower())
        return reverse('article_tag', args=[name])

class ArticleCategorySiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return models.Category.objects.filter(article__isnull=False).distinct()

    def location(self, item):
        name = slugify(item.name.lower())
        return reverse('article_category', args=[name])

class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return models.Project.objects.filter(date_published__lte=timezone.now())

    def lastmod(self, item):
        return item.updated

class ProjectTagSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return models.Tag.objects.filter(project__isnull=False).distinct()

    def location(self, item):
        name = slugify(item.name.lower())
        return reverse('project_tag', args=[name])

class StaticSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['articles', 'projects', 'about', 'contact', 'feed']

    def location(self, item):
        return reverse(item)
