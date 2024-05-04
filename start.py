import json
import matplotlib.pyplot as plt


PATH = 'data.json'


class Loader:
    """Получает json данные. Строит графики на основании данных."""
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Загрузить данные"""
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)

    def get_data(self):
        """Получить данные"""
        return self.data
    
    def create_plot(self, key: str):
        """Создать график"""
        if self.data is None:
            return 'Нет данных! Сначала нужно выполонить метод load_data.'
        if key not in self.data:
            return f'Ключ {key} отсутствует.'
        
        plt.plot(self.data['time'], self.data[key], label=key)
        plt.xlabel('time')
        plt.ylabel(key)
        plt.title(f'Зависимость {key} от time')
        plt.legend()
        plt.grid()
        plt.show()
        

l = Loader(PATH)
l.load_data()
data = l.get_data()

for key in data.keys():
    if key != 'time':
        l.create_plot(key)
