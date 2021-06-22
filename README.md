# Бот отслеживает появление товаров и снижение цен на WB.
![](gif/preview.gif)

Пример рабочего [бота](https://t.me/wildberries_helper_bot).


## Подготовка к работе.

Создайте два `telegram bot`. Для этого отправьте пользователю `@BotFather` в `Telegram` команды `/start` и затем `/newbot`. Вы получите API токен для доступа к боту. В дальнейшем токен первого бота запишете в переменную `TG_TOKEN`, этот бот будет помогать вам в отслеживании товаров. Токен второго запишете в `TG_LOGS_TOKEN` на него будут приходить логи в случае неисправностей. 
Получите ID чата. Для этого отправьте `@userinfobot` в `Telegram` команду `/start`. В ответ он пришлет `Id`. Его в дальнем вы запишете в переменную `TG_CHAT_ID`.

## Для запуска на локальной машине.
1. Создайте файл `.env` в головном каталоге. Внутри файла напишите 
```
TG_TOKEN=значение
TG_LOGS_TOKEN=значение
TG_CHAT_ID=значение

```
2. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
3. Запустите программу командой
```
python tg_bot.py
```
## Для запуска на платформе Heroku.

1. Сделайте `Fork` данного репозитория.
2. Зарегистрируйтесь на платформе [Heroku](https://signup.heroku.com/login). На [странице приложений](https://dashboard.heroku.com/apps) создайте новое. Затем во вкладке `Deploy` в пункте `Deployment method` выберите `GitHub`. Привяжите к`Heroku` ваш аккаунт `GitHub` и укажите путь к репозиторию.  Сделайте `Deploy`. Затем зайдите во вкладку `Settings` на странице приложения, найдите `Config Vars` и заполните переменные окружения по образцу:

имя переменной | значение |
--- | --- |
TG_TOKEN |	|
TG_LOGS_TOKEN |	|	
TG_CHAT_ID | |	

3. На странице приложения зайдите во вкладку `Resourses`.
Там вы увидете строку
```
 bot python3 tg_bot.py 
```
Справа от нее есть значок, при наведении подсветится `Edit dyno formation`. Зайдите и запустите программу.

