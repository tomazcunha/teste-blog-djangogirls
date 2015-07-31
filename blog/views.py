from django.shortcuts import render     # atalhos, médoto render

# Create your views here.

def post_list(request):     # aceitando um pedido
    return render(request, 'blog/post_list.html', {})   # retornando o html
