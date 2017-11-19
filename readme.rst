Сайт русскоязычного сообщества Write the Docs
=============================================

Чтобы собрать сайт на своей рабочей машине:

#.  Убедитесь, что в системе установлен Python 2
#.  В папке проекта создайте виртуальное окружение:

    ..  code-block:: bash

        virtualenv venv
        source virtualenv/bin/activate

#.  Установите необходимые зависимости

    ..  code-block:: bash

        pip install -r requirements.txt

#.  Соберите сайт из исходников:

    ..  code-block:: bash

        inv docs

#.  Откройте сайт в браузере:

    ..  code-block:: bash

        docs.browse

