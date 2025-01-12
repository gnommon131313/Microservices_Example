# Microservices_Example

* Глобальный ip и https для запуска в telegram mini apps можно получить с помошью `cloudflared tunnel --url http://localhost:80`
* Все запросы от фронтенда идут на localhost без порта, считаеться, что порт 80
* Использовать nginx (+нужно перекинуть файлы из nginx_conf в свой nginx/conf)
* Такое приложение будет работать коректно только на машине где запушен nginx (специфика локального ApiGateway)