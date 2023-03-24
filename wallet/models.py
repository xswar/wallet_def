from django.contrib.auth.models import User
from django.db import models

from config.settings import TRANSACTION_TYPES


class Account(models.Model):
    """ Моделька счета """
    name = models.CharField('Название счета', max_length=50, default="Счет")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Владелец')
    balance = models.IntegerField("Баланс", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class Tag(models.Model):
    """ Теги """
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Счет")
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.account.owner.username} - {self.account.name} - {self.category.name}"


class Image(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.transaction.account.name
