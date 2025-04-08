from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name




class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    card_image = models.ImageField(upload_to='cards/', default='cards/default.jpg')
    news_image = models.ImageField(upload_to='news/', default='news/default.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    categories = models.ManyToManyField(NewsCategory, related_name='news')

    FEATURED_CHOICES = [
        ('main', 'Main Featured'),
        ('side', 'Side Featured'),
        ('none', 'Not Featured')
    ]
    featured_type = models.CharField(
        max_length=10,
        choices=FEATURED_CHOICES,
        default='none'
    )


    def formatted_date(self):
        return self.pub_date.strftime("%d-%b-%Y")

    def __str__(self):
        return self.title



class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField(blank=True, null=True)
    columns = models.CharField(
        max_length=10,
        choices=[('main', "Main Ad"), ('others', "Other Ads")],
        default='main'
    )

    def __str__(self):
        return self.title



class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

