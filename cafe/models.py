from django.db import models

# COLORS_CHOICE = [
#     ('pink', 'pink'),
#     ('orange', 'orange'),
#     ('green', 'green'),
#     ('red', 'red'),
#     ('white', 'white'),
#     ('yellow', 'yellow'),
#     ('blue', 'blue'),
#     ('gold', 'gold'),
# ]

class Table(models.Model):
    table_number = models.IntegerField()
    top = models.IntegerField(default=0)
    left = models.IntegerField(default=0)
    label = models.CharField(max_length=20)
    color = models.CharField(max_length=50,
                            default='unselected-color')
    cafe = models.ForeignKey("Cafe", on_delete=models.CASCADE,
                            related_name='tables')

    def __str__(self):
        return str(self.cafe) + " " + self.label 
    

class Cafe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cafe', default='default.jpg')

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name
