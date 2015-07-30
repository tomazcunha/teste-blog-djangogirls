from django.contrib import admin
from .models import Post            # importando meu modelo Post

# Register your models here.

admin.site.register(Post)           # resgistrando o modelo no app admin 
