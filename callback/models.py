from django.db import models



class CallbackOrder(models.Model):
    userName = models.CharField('Имя',max_length=255, blank=False, default='Нет данных')
    userPhone = models.CharField('Телефон', max_length=255, blank=False, default='Нет данных')


    def __str__(self):
        return 'Форма заказа звонка. От {} '.format(self.userName)



    class Meta:
        verbose_name = "Форма заказа звонка"
        verbose_name_plural = "Формы заказа звонка"