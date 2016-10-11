# Eventex

Sistema de Eventos encomendando pela Morena.

[![Build Status](https://travis-ci.org/tyagow/eventex-revisao.svg?branch=master)](https://travis-ci.org/tyagow/eventex-revisao)  [![Code Health](https://landscape.io/github/tyagow/eventex-revisao/master/landscape.svg?style=flat)](https://landscape.io/github/tyagow/eventex-tyago/master)

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virutalenv com o Python 3.5
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Execute os testes.

```console
git clone git@github.com:tyagow/eventex-tyago.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy ?

1. Crie uma instancia no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG=False
5. Configure o servico de email
6. Envie o codigo para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# condigurar o email
git push heroku master --force
```