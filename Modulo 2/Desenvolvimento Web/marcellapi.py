import requests
item_cardapio={
'pizza'
"Hamburguer Suculento"
'feijoada'
'macarrao'
'pastel'
'coca'
'suco de laranja'
'fanta'
'agua com gas'
}
print(item_cardapio)
prato=input('digite seu pedido do cardapio')
bebida=input('digite a bebida')
mesa=input('digite a mesa')
    
pedido={
    'Prato':prato,
    'Bebida':bebida,
    'Mesa':mesa
    
   
}
    
requests.post('https://68c962feceef5a150f64a2a1.mockapi.io/Restaurante/',pedido)

requests.put('https://68c962feceef5a150f64a2a1.mockapi.io/Restaurante/9',pedido)









