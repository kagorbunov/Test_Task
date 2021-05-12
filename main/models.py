from django.db import models

# Create your models here.



class step(models.Model):

    step = models.CharField(max_length=50, verbose_name='Уровень выполнения')

    def __str__(self):
        return self.step

    class Meta:
        verbose_name = 'Уровень выполнения',
        verbose_name_plural = 'Уровни выполнения'





class priority(models.Model):

    priority = models.CharField(max_length=50, verbose_name='Приоритет выполнения', default=None, null=True)

    def __str__(self):
        return self.priority

    class Meta:
        verbose_name = 'Приоритет выполнения',
        verbose_name_plural = 'Приоритеты выполнения'




class todo(models.Model):
    title = models.CharField('Задача', max_length=255)
    description = models.TextField('Описание')
    data_start = models.DateTimeField('Дата начала', auto_now_add=True)
    data_end = models.DateTimeField('Дата окончания')
    step = models.ForeignKey(step, verbose_name = 'Уровень выполнения', on_delete=models.CASCADE)
    priority = models.ForeignKey(priority, verbose_name = 'Приоритет выполнения', on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {}".format(self.title, self.priority.priority)

    class Meta:
        verbose_name = 'Дело',
        verbose_name_plural = 'Дела'
