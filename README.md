# Free anti_spam_Telegram_bot

## anti_spam_Telegram_bot - Защитник Твоей группы!
 
### Автор: Den4yoo


### anti_spam_Telegram_bot - бот для отлова Url's спам ссылок в текстовых сообщениях. 

### Выполненные задачи:
 <br />
 <br />
 <br />
 <br />
 <br />


### Инструменты и стек технологий: <br /> 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 
## Запуск проекта на удалённом сервере: 
 
1. Подключение к удалённому серверу: 
```  
ssh -i путь_до_файла_с_SSH_ключом/название_файла_с_SSH_ключом имя_пользователя@ip_адрес_сервера  
```  
2. Создать директорию anti_4u
```  
sudo mkdir anti_4u 
```  
3. При необходимости почистить диск(кэш npm/APT/сист.логи): 
```  
npm cache clean --force 
```  
``` 
sudo apt clean 
```  
``` 
sudo journalctl --vacuum-time=1d 
```  
4. Устанавливаем Docker Compose на сервер (выполните команды поочерёдно): 
``` 
sudo apt update 
sudo apt install curl 
curl -fSL https://get.docker.com -o get-docker.sh 
sudo sh ./get-docker.sh 
sudo apt install docker-compose-plugin 
``` 
5. Скопируйте на сервер в директорию anti_4u/ файл docker-compose.production.yml: 
``` 
scp -i path_to_SSH/SSH_name docker-compose.production.yml \ 
    username@server_ip:/home/username/anti_4u/docker-compose.production.yml 
``` 
6. Cоздать файл .env (в директории /anti_4u), содержащий пары ключ-значение всех переменных окружения. 
```  
POSTGRES_USER=*** <br /> 
POSTGRES_PASSWORD=*** <br /> 
POSTGRES_DB=*** <br /> 
DB_HOST=*** <br /> 
DB_PORT=*** <br /> 
API_KEY=*** <br /> 
DEBUG=*** <br /> 
ALLOWED_HOSTS=*** <br /> 
```  
7. Запуск Docker Compose в режиме демона: 
``` 
sudo docker compose -f docker-compose.production.yml up -d 
``` 
8. Выполните миграции, соберите статические файлы бэкенда и скопируйте их в /backend_static/static/: 
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic 
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/ 
``` 
9. Настройте и перезагрузите конфиг Nginx: 
``` 
sudo nano /etc/nginx/sites-enabled/default 
``` 
``` 
sudo service nginx reload 
``` 

 
## Автоматический деплой проекта на сервер. 
Для автоматического деплоя проекта на сервер с помощью GitHub actions необходимо добавить SECRETS в свой репозиторий: 
 
• DOCKER_PASSWORD=<пароль от DockerHub> <br /> 
• DOCKER_USERNAME=<имя пользователя DockerHub> <br /> 
• HOST=<ip сервера> <br /> 
• SSH_KEY=<приватный SSH-ключ> <br /> 
• SSH_PASSPHRASE=<пароль для сервера> <br /> 
• TELEGRAM_TO=<id Телеграм-аккаунта> <br /> 
• TELEGRAM_TOKEN=<токен  бота> <br /> 
• USER=<username для подключения к удаленному серверу> <br /> 
