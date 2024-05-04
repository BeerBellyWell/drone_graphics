import json
import matplotlib.pyplot as plt

# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

with open('data.json', 'r') as file:
    data = json.load(file)

# Зависимость error_x от time
line_1 = plt.subplot(2, 3, 1)
plt.plot(data['time'], data['error_x'], color='r', label='error_x')
plt.xlabel('time')
plt.ylabel('error x')
plt.title('Зависимость error_x от time')
plt.legend()

# Зависимость error_y от time
line_2 = plt.subplot(2, 3, 2)
plt.plot(data['time'], data['error_y'], color='r', label='error_y')
plt.xlabel('time')
plt.ylabel('error y')
plt.title('Зависимость error_y от time')
plt.legend()

# Зависимость yaw от time
line_3 = plt.subplot(2, 3, 3)
plt.plot(data['time'], data['yaw'], color='b', label='yaw')
plt.xlabel('time')
plt.ylabel('yaw')
plt.title('Зависимость yaw от time')
plt.legend()

# Зависимость pitch от time
line_4 = plt.subplot(2, 3, 4)
plt.plot(data['time'], data['pitch'], color='g', label='pitch')
plt.xlabel('time')
plt.ylabel('pitch')
plt.title('Зависимость pitch от time')
plt.legend()

# Зависимость throttle от time
line_5 = plt.subplot(2, 3, 5)
plt.plot(data['time'], data['throttle'], color='c', label='throttle')
plt.xlabel('time')
plt.ylabel('throttle')
plt.title('Зависимость throttle от time')
plt.legend()

# Зависимость roll от time
line_6 = plt.subplot(2, 3, 6)
plt.plot(data['time'], data['roll'], color='m', label='roll')
plt.xlabel('time')
plt.ylabel('roll')
plt.title('Зависимость roll от time')
plt.legend()

line_1.grid()
line_2.grid()
line_3.grid()
line_4.grid()
line_5.grid()
line_6.grid()

plt.tight_layout()
plt.show()


