from django.db import models

# Boutique
class Categorie(models.Model):
    nom	 = models.CharField(default="",max_length=200)

    class Meta:
        verbose_name = "Categorie"
        ordering = ['nom']

    def __str__(self):
        return self.nom

    def get_article(self):
        return Article.objects.filter(categorie=self)

class Article(models.Model):
    nom	        = models.CharField(default="",max_length=200)
    image       = models.FileField(upload_to='Articles/', max_length=200, blank=True, null=True)
    categorie   = models.ForeignKey(Categorie, blank=True, null=True, on_delete=models.SET_NULL)
    prix	    = models.FloatField(default=0)
    unite	    = models.CharField(default="",max_length=200)
    description = models.TextField(default="", blank=True, null=True)
    date_creation  = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = "Article"
        ordering = ['nom']

    def __str__(self):
        return self.nom