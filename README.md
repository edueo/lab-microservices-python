# lab-microservices-python

# Quart 

Evolução do Flask com suporte assíncrono

repositório: https://github.com/pallets/quart
documentação: https://quart.palletsprojects.com/en/latest/


## Instalação 

Criar arquivo requirements.in, com o conteúdo:
```
quart==0.19.4
```
gerar o arquivo das dependências usando o comando:
`pip-compile requirements.in`

## ASGI vs WSGI

requisições -> mecanismo -> código python

interface entre o webserver e o código python

## Request

No Quart é uma variável global, mas é única para cada requisição e **thread-safe**. 
