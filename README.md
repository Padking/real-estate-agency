# Real estate agency

Урок № 5 модуля "Знакомство с Django: ORM" от Devman.

## Описание

Сайт подбора недвижимости и редактирования информации о ней

### Особенности

- позволяет выбрать объявление о продаже квартиры на основе фильтров:
    * город,
    * новостройка или нет,
    * цена "от"/"до"
- предоставляет возможность:
    * создать/редактировать жалобу на [квартиру](https://github.com/Padking/real-estate-agency/wiki#%D0%9F%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F),
    * создать/редактировать собственника квартиры,
    * выполнить поиск собственника по: ФИО, нормализованному номеру телефона,
    * создать/редактировать квартиру,
    * выполнить поиск квартиры по: названию города, адресу квартиры,
    * использовать фильтрацию квартир по: принадлежности к новостройке, кол-ву комнат, наличию балкона,
    * оценить квартиру лайком

## Примеры использования

  Поиск объявления на основе фильтров:

  ![site_1_search_flat](https://github.com/Padking/real-estate-agency/blob/master/screenshots/site_1_search_flat.png)


  Создать/редактировать жалобу:

  ![site_2_create_edit_claim](https://github.com/Padking/real-estate-agency/blob/master/screenshots/site_2_create_edit_claim.png)


  Создать/редактировать собственника:

  ![site_2_create_edit_owner](https://github.com/Padking/real-estate-agency/blob/master/screenshots/site_2_create_edit_owner.png)


  Поиск собственника по ФИО:

  ![site_2_search_by_owners_fullname](https://github.com/Padking/real-estate-agency/blob/master/screenshots/site_2_search_by_owners_fullname.png)


  Создать/редактировать квартиру:

  ![site_2_create_edit_flat](https://github.com/Padking/real-estate-agency/blob/master/screenshots/site_2_create_edit_flat.png)


  Поиск квартиры по названию города:

  ![site_2_search_by_flats_town](https://github.com/Padking/real-estate-agency/blob/master/screenshots/site_2_search_by_flats_town.png)


  Выделение новостроек из общего числа квартир:

  ![site_2_segregation_flats_by_new_building](https://github.com/Padking/real-estate-agency/blob/master/screenshots/site_2_segregation_flats_by_new_building.png)


## Предметная область

  Схема сущностей БД:

  ![db_schema](https://github.com/Padking/real-estate-agency/blob/master/screenshots/db_schema.png)

## Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно указать их в файле `.env`.
Передача значений ПеО происходит с использованием [environs](https://pypi.org/project/environs/).

### Параметры проекта

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`ALLOWED_HOSTS`| Разрешённые хосты |`['0.0.0.0', '127.0.0.1', 'localhost']`|
|`DEBUG`| Режим отладки |`True`|
|`SECRET_KEY`| Уникальное непредсказуемое значение |-|

### Параметры подключения к БД

По умолчанию, используется СУБД SQLite.

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DATABASE`| [Однострочный](https://github.com/jacobian/dj-database-url) адрес к базе данных | - |

## Установка

- Клонирование проекта,
- создание каталога виртуального окружения (ВО)*,
- связывание каталогов ВО и проекта,
- установка зависимостей:
```bash
git clone https://github.com/Padking/real-estate-agency.git
cd real-estate-agency
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt
```

- применение миграций к проекту:
```bash
python manage.py migrate
```

- создание суперпользователя в интерактивном режиме**,
- наполнение БД информацией о квартирах и собственниках через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/),
- запуск сайта,
- переход на [сайт](http://127.0.0.1:8000/admin/) для наполения БД,
- убедиться в наличии объявлений на [сайте](http://127.0.0.1:8000/).
```bash
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```



\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

\** для наполнения БД через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
