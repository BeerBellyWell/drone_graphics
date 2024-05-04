# Drone graphics
Строит графики по полученным данным.

#### Как запустить проект:

+ клонируем репозиторий `git clone`
`https://github.com/BeerBellyWell/drone_graphics.git`
+ переходим в него `cd drone_graphics`
    + разворачиваем виртуальное окружение
    `python3 -m venv env` (Windows: `python -m venv env`)
    + активируем его
    `source env/bin/activate` (Windows: `source env/scripts/activate`)
    + устанавливаем зависимости из файла requirements.txt
    `pip install -r requirements.txt`

#### Как запустить проект:
+ `python start_simple.py` - Построит все графики в одном окне.
+ `python start.py` - Реализация через ООП. Создан класс, который загружает данные из JSON-файла. Построение графиков реализовано через методы класса. Графики визуализируются по одному.