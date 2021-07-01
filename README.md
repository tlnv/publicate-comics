# Публикуйте комиксы Вконтакте
В данном проекте реализована автоматизация публикации контента в сообществе Вконтакте.
### Как установить
Python 3 должен уже быть установлен. Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```
### Как настроить окружение
Для настройки окружения вам необходимо выполнить следующие действия:
1. [Создать свое приложение](https://vk.com/apps?act=manage).
2. Получить client_id приложения: зайти в ["Мои приложения"](https://vk.com/apps?act=manage) --> "Редактировать" --> "Настройки" --> "ID приложения"
3. Осуществить процедуру Implicit Flow: в web-браузере перейти по ссылке https://oauth.vk.com/authorize?client_id=ваш client_id&display=page&scope=friends,photos,groups,wall,offline&response_type=token&v=5.131
4. После перехода по ссылке вы получите `access_token` , который необходимо присвоить переменной `VK_ACCESS_TOKEN` в файле `.env`.
5. Создать сообщество Вконтакте, [получить его ID](https://regvk.com/id/), и присвоить его переменной `VK_GROUP_ID` в файле `.env`.
```
VK_ACCESS_TOKEN=a666046qv6405ac68c37b965f8835b43c2c9bf0fa3ecb4d9da3a5a85989ebabd042e880701d6f7f687f4b1
```
### Как пользоваться скриптом
Для запуска скрипта воспользуйтесь примером запуска из консоли. 

В `def main()` функция `post_wall.post_photo(file, message)` принимает на вход изображение в форматах .jpg, .png, .gif и текст, который будет комментарием для этого изображения. В проекте в качестве контента для постинга используются случайно выбранные комиксы с сайта [xkcd.com](https://xkcd.com).
Вы можете поменять или добавить свой источник контента, написав код, который будет возвращать изображение и текст. Для примера возьмите `fetch_comics.py`, и замените параметры согласно API сайта, с которым вы работаете. 

### Пример запуска из консоли
```
$ python main.py
```
### Цель проекта
Код написан в образовательных целях на онлайн курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)