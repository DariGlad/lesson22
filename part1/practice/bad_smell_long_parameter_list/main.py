# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x: int, y: int, speed=1):
        self.field = field
        self.x = x
        self.y = y
        self.speed = speed

    def _get_speed(self, state):
        if state == "FLY":
            return self.speed * 1.2
        elif state == "CRAWL":
            return self.speed * 0.5
        else:
            raise ValueError("Рожденный ползать летать не может!")

    def move(self, state: str, direction: str):

        new_y = 0
        new_x = 0

        speed = self._get_speed(state)

        if direction == 'UP':
            new_y = self.y + speed
            new_x = self.x
        elif direction == 'DOWN':
            new_y = self.y - speed
            new_x = self.x
        elif direction == 'LEFT':
            new_y = self.y
            new_x = self.x - speed
        elif direction == 'RIGTH':
            new_y = self.y
            new_x = self.x + speed

        self.field.set_unit(x=new_x, y=new_y, unit=self)
