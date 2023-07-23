# Космический Телеграм
В проекте представлены скрипты для скачивания изображений: запусков SpaceX, изображений дня и EPIC изображений с сайта NASA. Далее эти фотографии с помощью телеграм-бота можно опубликовать в телеграм-канале о Cosmos Photo.


## Как установить
Для скачивания фотографий EPIC и APOD с [сайта](https://nasa.gov/) нужно получить токен для допуска к API.
Для этого необхлдимо перейти по [ссылке](https://api.nasa.gov/)  и зарегестрироваться, следуя инструкции на сайте.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл .env рядом остальными файлами кода  
и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступна 1 переменная:
* API_ID - токен полученный при регистрации на [сайте](https://api.nasa.gov/)


#### Запуск скрипта
* Для запуска скрипта для скачивания SpaceX запусков:
  
   ```
  py fetch_spacex_images.py 5eb87d42ffd86e000604b384
   ```
    Здесь нужно знать ID запуска. Подробнее о нем можно почитать [here](https://github.com/r-spacex/SpaceX-API/blob/master/docs/launches/v5/all.md)
* Для запуска скрипта для скачивания APOD:  
   ```
  py fetch_APOD.py 6
   ```  
  Здесь нужно указать количество фотографий, которое требуется скачать.
* Для запуска скрипта для скачивания EPIC:
    ```
  py fetch_EPIC.py 10
    ```  
   Здесь нужно указать количество фотографий, которое требуется скачать.
* Для запуска скрипта для публикации фотографий:
  ```
  py telegram_bot.py 1
  ```
  Здесь нужно указать временной интервал для публикаций фото.
* Для запуска скрипта для публикации определенной фотографии:
  ```
  py post_certain_image.py 23.png
  ```
  Здесь нужно указать имя фотографии, которую надо опубликовать.


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.