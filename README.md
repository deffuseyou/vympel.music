# vympel.music
Сайт на Flask для сбора сообщений и голосования за песни

## Установка
1. Узнайте токен авторизации от своего роутер TP-LINK. Сделать это можно через WireShark, выглядит он так:
```Authorization\=Basic%20Z#########################################################%3D%3D```
2. Создайте [бота Telegram](https://t.me/botfather) и скопируйте токен
3. Заполните переменныо окружения `router_auth_token` `vm_bot_token` соответствующими значениями
4. В `ids.txt` перечислите все __telegram_id__ с новой строки, которым нужно отправлять сообщения
