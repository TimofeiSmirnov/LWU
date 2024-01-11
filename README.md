# LWU как запустить на своем устройстве

1. Установить питон и гит
2. Скопировать директорию себе локльно git clone [https://github.com/TimofeiSmirnov/LWU.git] и зайти в неё
3. Создать venv (дириктория для запуска пинота + менеджер библиотек проекта) python3 -m venv venv и активировать его source venv/bin/activate
4. Установть все зависимоти pip install -r requirements.txt
5. Запустить app.py python3 app.py


[ Как добавть зависимость? ]

1. при работающем venv'е запустить команду pip install YOUR_LIB_NAME
2. добавить название библиотеки в requirements.txt cо строгим указанием версии
