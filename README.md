# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Требования
Должны быть установлены:
- git, чтобы вы могли скачать код; 
- python3, чтобы вы могли запустить код. 

## Запуск

Скачайте код с помощью команды в командной строке
```
git clone https://github.com/Boltasov/devman_wine
```
Установите необходимые библиотеки командой
```
python pip install -r requirements.txt
```
Поместите таблицу с винами в папку с файлом `main.py` и переименуйте таблицу в `wine.xlsx`. Пример таблицы приведён в файле `wine.xlsx` данного репозитория.

По умолчанию в качестве источника данных будет использоваться файл, размещённый указанным выше способом. Если вы хотите использовать файл по другому пути, то создайте файл с названием `.env` и разместите туда следующий текст:
```
FILE_PATH='put_here_your_path'
```
Для примера это может быть `tables\wine.xlsx` при работе в Windows.

Запустите сайт командой 
```
python main.py`
``` 
Cайт можно будет открыть по адресу [http://127.0.0.1:8000/index.html](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
