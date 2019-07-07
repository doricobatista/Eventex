# Eventex

Sistema de eventos (aula WTTD) encomendado pela 'Morena'.

## Como desenvolver?

1. CLone o repositório
2. Crie um virtualenv com Python 3.7
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instância com o .env (Variáveis de ambiente)
6. Execute os testes

´´´
git clone git@github.com:doricobatista/eventex.git sistema
cd sistema
python -m venv .pd3.7
source .dp3.7/bin/activate
pip install -r requeriments.txt
cp contrib/env-sample .env
python manage.py test
´´´

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

´´´console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py' # dica: gerar em hbn.link/secret_gen
heroku config:set DEBUG=False
# Configurar Email
git push heroku master --force

´´´