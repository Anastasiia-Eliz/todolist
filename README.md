Todolist
Предварительные требования к будущему приложению
 1. Вход/регистрация/аутентификация через вк. 
 2. Создание целей.
1)Выбор временного интервала цели с отображением кол-ва дней до завершения цели.
2)Выбор категории цели (личные, работа, развитие, спорт и т. п.) с возможностью добавлять/удалять/обновлять категории.
3)Выбор приоритета цели (статичный список minor, major, critical и т. п.).
4)Выбор статуса выполнения цели (в работе, выполнен, просрочен, в архиве).
 3. Изменение целей.
1)Изменение описания цели.
2)Изменение статуса.
3)Дать возможность менять приоритет и категорию у цели.
 4. Удаление цели.
1)При удалении цель меняет статус на «в архиве».
 5. Поиск по названию цели. 
 6. Фильтрация по статусу, категории, приоритету, году.
 7. Выгрузка целей в CSV/JSON. 
 8. Заметки к целям.
 9. Все перечисленный функции должны быть реализованы в мобильном приложении.

Стек 
- django - backend
- postgresql - database

Как запустить проект:
Создать виртуальное окружение.
Установить зависимости, указанные в файле requirements.txt:
- pip install -r requirements.txt
Установите переменные среды в файле .env 
- создайте файл .env в папке корневой папке todolist
скопировать переменные по умолчанию можно из todolist/.env
Запустите базу данных:
выполнить команду docker-compose up --build -d
Накатить миграции:
python ./manage.py makemigraitons
python ./manage.py migrate
Запустить проект
python ./manage.py runserver