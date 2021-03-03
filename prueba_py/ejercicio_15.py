import requests
import json

print('\nMétodo GET:')
URL_BASE = 'https://jsonplaceholder.typicode.com/users'
r_get = requests.get(URL_BASE)
if r_get.status_code == 200:
    datos = r_get.json()
    cont = 0
    for usario in datos:
        print('Nombre de usuario: {}, alias: {}, email: {}, ciudad: {} '.format(usario['name'], usario['username'], usario['email'], usario['address']['city']) )
        cont += 1
    print('Número de usuarios existentes:',cont)
else:
    print('Error: {} en la consulta GET'.format(r_get.status_code))

print('\nMétodo POST:')
URL_BASE = 'https://jsonplaceholder.typicode.com/comments'
informacion = {'postId':1, 'name':"Cualquiera", 'email':"inventado@hotmail.com", 'body':"Comentario sobre el tiempo"}
r_post = requests.post(URL_BASE, data = informacion)
if r_post.status_code == 201:
    datos = r_post.json()
    print('Comentario añadido:',datos)
else:
    print('Error: {} al hacer el comentario POST'.format(r_post.status_code))
