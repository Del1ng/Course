import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.happiness = 100
        self.satiety = 100
        self.house = None
        self.job = None

    def housse(self, house):
        self.house = house

    def eat(self):
        if self.satiety < 100 and self.house.food > 0:
            self.satiety += 10  
            self.happiness += 5  
            self.house.food -= 1  # Уменьшаем количество еды в доме
            print(f"{self.name} поел. Сытость: {self.satiety}, Счастье: {self.happiness}, Еда в доме: {self.house.food}")
        else:
            print(f"{self.name} не может поесть. Сытость: {self.satiety}, Еда в доме: {self.house.food}")
    
    def work(self):
        if self.job is None:
            print(f"{self.name} не имеет работы.")
            return
        
    def jizn(self):
        if self.satiety <= 0 or self.happiness <= 0:
            print(f"{self.name} не смог выжить.")
            return False
        return True

class House:
    def __init__(self):
        self.mess = 0
        self.food = 5  

house = House()
human = Human("Alexandr")
human.job = "Программист"  


vibor = {
    "1": human.eat,
    "2": human.work
}

for day in range(1, 100):
    print(f"\nДень {day}:")
    print("Действие: ")
    print("1: Покушать")
    print("2: Работать")
    
    viborr = input("Введите действие: ")
    
    if viborr in vibor:
        vibor[viborr]()  
    else:
        print("Неверное действие.")
    
    if not human.jizn():  
        break