import requests
# Requsiçao que traz os pedidos
dados=requests.get( 'https://68c962feceef5a150f64a2a1.mockapi.io/Restaurante/')
print(dados.json())

# requsisçao que exclui o pedido 
excluir=input('digite qualpedido deseja remover')
requests.delete(f'https://68c962feceef5a150f64a2a1.mockapi.io/Restaurante/{excluir}')
 