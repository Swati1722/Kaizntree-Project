
from django.db import models

        
class Items(models.Model):

    sku = models.CharField(max_length=100, null=True, blank=True, help_text="SKU")
    
    name = models.CharField(max_length=100, null=True, blank=True, help_text="Name of SKU")
    
    tags = models.ManyToManyField('Tag', blank=True, help_text="Tags associated with the item")
    
    category = models.ManyToManyField('Category' , max_length=100, null=True, blank=True, help_text="Category of SKU")
    
    in_stocks = models.IntegerField(default=0, null=True, blank=True, help_text="Number of total stocks")
    
    available_stocks = models.IntegerField(default=0, null=True, blank=True, help_text="Available stocks")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        
    def get_all_tags(self):
        try:
            tag_objs = self.tags.all()
            tag_str = ""
            for i in tag_objs:
                tag_str += i.name + " "
            return tag_str
        except Exception as e:
            print("Error in get_all_tags ", e)
    
    def get_all_categories(self):
        try:
            category_objs = self.category.all()
            category_str = ""
            for i in category_objs:
                category_str += i.name + " "
            return category_str
        except Exception as e:
            print("Error in get_all_categories ", e)


class Tag(models.Model):
    
    name = models.CharField(max_length=50, unique=True, help_text="Tag name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Category(models.Model):
    
    name = models.CharField(max_length=50, unique=True, help_text="Category name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
