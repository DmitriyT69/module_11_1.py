import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


class Requests:
    print('-----------------------------------------------------------------------')
    url = 'https://tinkoff.ru'  # Указываем URL, на который будем отправлять GET-запрос

    response = requests.get(url)  # Отправляем GET-запрос по указанному URL

    if response.status_code == 200:  # Проверяем статус-код ответа

        data = response.url  # Если статус-код 200 (OK), получаем данные из ответа
        print(f'Статус ответа: OK [код 200]')

    else:
        print('Ошибка при выполнении запроса')  # В случае ошибки выводим сообщение


print('-----------------------------------------------------------------------')


class Panda:
    # Загрузка данных из текстового файла
    data = pd.read_fwf(r'C:\Users\Ильдус\PycharmProjects\obzor_storonnih_bibliotek_python\Readme')

    # Отображение первых 5 строк данных
    print(data.head())


print('-----------------------------------------------------------------------')


class Numpy:
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Создаем массив
    sum = np.sum(arr)  # Суммируем его элементы
    flip = np.flip(arr)  # Элементы массива в обратном порядке

    print(arr)
    print(sum)
    print(flip)


print('-----------------------------------------------------------------------')


class Matplotlib:
    x = [5, 4, 3, 2, 1]  # Задаем данные по осям
    y = [10, 20, 15, 25, 30]

    plt.plot(x, y)  # Построение линейного графика
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title('Пример линейного графика')
    plt.show()


class Pillow:
    image = Image.open(r'C:\Users\Ильдус\PycharmProjects\obzor_storonnih_bibliotek_python\auto.jpg')
    resized_image = image.resize((800, 600))  # изменение размера на 800 x 600 пикселей
    resized_image.save('resized_image.jpg')

    # image = Image.open(r'C:\Users\Ильдус\PycharmProjects\obzor_storonnih_bibliotek_python\auto.jpg')
    blurred_image = image.filter(ImageFilter.BLUR)  # применить эффекты
    blurred_image.save('blurred_image.jpg')

    # сохранить в другой формат
    # image = Image.open(r'C:\Users\Ильдус\PycharmProjects\obzor_storonnih_bibliotek_python\auto.jpg')
    image.save('converted_image.jpg')  # конвертация в формат JPEG
    image.save('converted_image.gif')  # конвертация в формат GIF
