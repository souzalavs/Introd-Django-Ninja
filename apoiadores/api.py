from ninja import NinjaAPI
from .models import Apoiador

api = NinjaAPI()

@api.get('apoiador/')
def listar(request):
    apoiador = Apoiador.objects.all()
    response = [{'id' : i.id, 'nome' : i.nome, 'mensagem' : i.mensagem} for i in apoiador]
    return response
