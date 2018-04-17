# flask_api jsonrpc documentation

_Flask cli команды_

```flask``` - получить список доступных команд

```flask db current``` - версия миграции

```flask db migrate``` - произвести миграцию

```flask db upgrade``` - накатить миграцию

```flask db downgrade``` - откатить миграцию

```flask tests_run``` - запуск unittests в консоли

_Cамописные cli команды находятся в директории /utils/cli, для удобства выполняемые функции вынесены в директорию /cli_handlers.Рекомендуется все скрипты реализовывать именно через cli_

**Cтарт api**

```
export FLASK_APP=manage.py

flask run
```

```flask run --host=0.0.0.0 --port=80``` - запуск не на default порту

_Запуск через .sh скрипт : создать в директории проекта start.sh с содержимым, указав dev или prod  флаг_

```
#!/usr/bin/env bash

export FLASK_CONFIGURATION="dev"
 
python manage.py
```
 
_Запустить bash ./start.sh(из корня) в виртуальном окружении_

**Старт celery (sms и email оповещения)**

```celery -A celery_tasks.notifications_tasks worker -l info```

_Старт/Стоп в фоновом режиме_

```celery multi start w1 -A celery_tasks.notifications_tasks -l info```

```celery multi stop w1 -A celery_tasks.notifications_tasks -l info```

**Запуск celery (xml фиды)**

```
celery -A celery_tasks.ad_export_tasks worker -B -l info -s /sites/api.spn.market/logs/celerybeat-schedule
```

_Старт/Стоп в фоновом режиме_

```
celery multi start w1 -A celery_tasks.ad_export_tasks worker -B -l info -s /sites/api.spn.market/logs/celerybeat-schedule
```

```
celery multi stop w1 -A -A celery_tasks.ad_export_tasks worker -B -l info -s /sites/api.spn.market/logs/celerybeat-schedule
```


### Дополнительные утилиты для взаимодействия с внешними api и другие полезные функции, классы и хелперы - находятся в дирректории /utils

