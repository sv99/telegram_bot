Telegram Bot
============

pipenv
------

https://pipenv.kennethreitz.org/en/latest/

Using pipenv with `Pipfile` and `Pipfile.lock`

```bash
# Install from pip
pip install pipenv
pipenv install aiogram
pipenv install pytest --dev
pipenv uninstall numpy
# Install all
pipenv install
# show dependency graph
pipenv graph
# show venv info
pipenv --venv
```

bot.py
------

https://github.com/eternnoir/pyTelegramBotAPI

https://groosha.gitbook.io/telegram-bot-lessons/ - pyTelegramBotAPI

Бот на базе pyTelegramBotAPI.

В pyTelegramBotAPI нет поддержки FSM. 

bot_ai.py
---------

https://aiogram.readthedocs.io/en/latest/index.html

https://surik00.gitbooks.io/aiogram-lessons/content/ - aiogram

Бот на базе aiogram - полностью асинхронная библиотека.

Встроенная поддержка FSM, три варианта хранилища текущего
состояния FSM. Сразу можно привязать обработчики к состояниям.

Неполная документация, особенно в части касающейся дополнительных возможностей.

