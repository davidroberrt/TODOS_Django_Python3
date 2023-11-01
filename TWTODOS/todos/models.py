from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)   #CharField é para virar char string no banco de dados / max_length #quantidade de caracteres / null=Flase : o campo no banco de dados nao pode ter valores nulos, blank=False) não pode conter string vazia ou espaços em branco# Create your models here.
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) # na hora que o todo for cadastrado, vai ser naqeuele momento
    deadline = models.DateTimeField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True)