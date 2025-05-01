import random

IMAGE_PATH_1 = 'styles/images/cat_1.jpeg'
IMAGE_PATH_2 = 'styles/images/cat_2.jpeg'
IMAGE_PATH_3 = 'styles/images/cat_3.jpeg'

class Cat:
    name = ''
    age = 1
    happiness = 40
    satiety = 40
    image = IMAGE_PATH_1
    is_sleeping = False

    @classmethod
    def put_limits(cls):
        try:
            if cls.happiness > 120 or cls.satiety > 100:
                raise ValueError('Показания превысили 100')
        except:
            print('Обрабатываю данные')



    @classmethod
    def image_display(cls):
        if cls.happiness <= 30:
            cls.image = IMAGE_PATH_2
        elif 30 < cls.happiness <= 60:
            cls.image = IMAGE_PATH_3
        else:
            cls.image = IMAGE_PATH_1
        cls.put_limits()


    @classmethod
    def play(cls):
        random_chance = random.randint(1, 3)
        if random_chance != 1:
            if cls.is_sleeping is True:
                cls.happiness -= 5
            else:
                cls.happiness += 15
                cls.satiety -= 10
        else:
            cls.happiness = 0
        cls.image_display()
        cls.put_limits()


    @classmethod
    def feed(cls):
        if cls.is_sleeping is True:
            print('Спящего кота нельзя покормить')
        else:
            cls.happiness += 5
            cls.satiety += 15
            if cls.satiety >= 100:
                cls.happiness -= 30
        cls.image_display()
        cls.put_limits()

    @classmethod
    def sleep(cls):
        cls.image_display()

    def cheer_up(cls):
        cls.image_display()