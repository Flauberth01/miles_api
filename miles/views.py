from django.http import JsonResponse


def depoimentos(request): #TODO: request sabe de tudo.
    """Depoimentos"""
    if request.method == 'GET':
        depoimento = {'id':1, 'nome': 'flauberth'}
        return JsonResponse(depoimento)
