from django.db import models

# class Log(models.Model):
#     logDate = models.DateTimeField()
#     scrapedSource = models.CharField(max_length=255)
#     nbOfArticles = models.PositiveIntegerField()

#     def __str__(self):
#         return f"Log {self.id} - {self.scrapedSource}"

# class Article(models.Model):
#     timeCreated = models.DateTimeField()
#     headline = models.CharField(max_length=255)
#     thumbnail = models.URLField(blank=True, null=True)
#     body = models.TextField()
#     log = models.OneToOneField(Log, on_delete=models.CASCADE, related_name='article')

#     def __str__(self):
#         return self.headline

class Log(models.Model):
    logDate = models.DateTimeField(auto_now_add=True)
    scrapedSource = models.CharField(max_length=255)
    nbOfArticles = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.scrapedSource} - {self.logDate.strftime('%Y-%m-%d %H:%M')}"

class Article(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, related_name='articles')
    title = models.TextField()
    url = models.URLField(unique=True)
    content = models.TextField(blank=True)
    source = models.CharField(max_length=255)
    date_scraped = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

