import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.happines = 100
        self.satiety = 100
        self.house = None
        self.job = None
        self.repair_kits = 0  # Количество ремкомплектов у человека

    def housse(self, house):
        self.house = house
        
    def na_job(self, job):
        self.job = job

    def eat(self):
        if self.satiety < 100 and self.house.food > 0:
            self.satiety += 20  
            self.happines += 10 
            self.house.food -= 1
            print(f"{self.name} поел. Сытость: {self.satiety}, Счастье: {self.happines}")
        else:
            print(f"{self.name} не может поесть. Сытость: {self.satiety}, еда: {self.house.food}")
    
    def work(self):
        if self.job:
            self.money += self.job.salary
            self.happines -= 20
            self.satiety -= 10
            print(f"{self.name} работал. Деньги: {self.money}, Счастье: {self.happines}, Сытость: {self.satiety}")
        else:
            print(f"У {self.name} нет работы.")
        
    def shop(self):
        print("-" *20)
        print(f"Добро пожаловать в магазин, {self.name}!")
        print("Что хотите купить?")
        print("1: Еда (20 денег 1 штука)")
        print("2: Купить ремкомплект для машины (50 денег за 1 штуку)")
        print("3: Выйти из магазина")
        
        while True:
            c = input("Введите действие: ")
            
            if c == "1":
                if self.money >= 20:
                    self.money -= 20
                    self.house.food += 1
                    self.satiety -= 10
                    print(f"{self.name} купил 1 ед. еды. Деньги: {self.money}, Еда в доме: {self.house.food}")
                    print("-" *20)
                elif self.money < 20:
                    print(f"У вас недостаточно денег для покупки еды.")
                    print("-" *20)
            elif c == "2":
                if self.money >= 50:
                    self.money -= 50
                    self.satiety -= 10
                    self.repair_kits += 1  
                    print(f"{self.name} купил 1 ед. ремкомплекта. Деньги: {self.money}, Ремкомплектов на руках: {self.repair_kits}")
                    print("-" *20)
                else:
                    print(f"У вас недостаточно денег для покупки ремкомплекта.")
                    print("-" *20)
            elif c == "3":
                print(f"{self.name} покинул магазин.")
                print("-" *20)
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
                print("-" *20)

    def jizn(self):
        if self.satiety <= 0 or self.happines <= 0:
            print(f"{self.name} не смог выжить.")
            return False
        return True
    
    def status(self):
        print(f"Имя {self.name}: Деньги: {self.money}, Счастье: {self.happines}, Сытость: {self.satiety}, Еда в доме: {self.house.food}, Ремкомплекты: {self.repair_kits}")
    

# Машина
class Auto:
    def __init__(self, brand, fuel, durability, fuel_consumption):
        self.brand = brand
        self.fuel = fuel
        self.durability = durability
        self.fuel_consumption = fuel_consumption
        
    def move(self):
        if self.fuel > self.fuel_consumption and self.durability > 15:
            self.fuel -= self.fuel_consumption  
            print(f"{self.brand} двигается. Оставшееся топливо: {self.fuel}")
            
        elif self.durability <= 15:
            print(f"{self.brand} слишком повреждён. Нужно отремонтировать машину.")
            self.repair()
        else:
            print(f"{self.brand} не может двигаться. Недостаточно топлива.")
        
    # Ремонт
    def repair(self):
        if human.repair_kits > 0: 
            print(f"{self.brand} ремонтируется...")
            self.durability = 100  
            human.repair_kits -= 1 
            print(f"{self.brand} отремонтирован. Прочность восстановлена. Прочность: {self.durability}. Осталось ремкомплектов: {human.repair_kits}")
        else:
            print(f"У вас нет ремкомплектов для ремонта {self.brand}.")
        
    # Статус машины
    def car_status(self):
        print(f"Бренд: {self.brand}, Топливо: {self.fuel}, Прочность: {self.durability}")


class Job:
    def __init__(self, salary):
        self.salary = salary

class House:
    def __init__(self):
        self.food = 0
        self.repair_kits = 0

car = Auto("Toyota", 50, 30, 5)  
house = House()
job = Job(100)
human = Human("Alexandr")
human.na_job(job)
human.housse(house)

vibor = {
    "1": human.eat,
    "2": human.work,
    "3": human.shop,
    "4": car.car_status,  
    "5": car.move,
    "6": car.repair,  
}

for day in range(1, 100):
    human.status()
    print(f"День {day}:")
    print("Действие: ")
    print("1: Покушать")
    print("2: Работать")
    print("3: Магазин")
    print("4: Статус машины")
    print("5: Поездить на машине")
    print("6: Починить машину")
    
    while True:
        viborr = input("Введите действие: ")
        if viborr in vibor:
            vibor[viborr]()  
            print("-" *20)
            break
        else:
            print("Неверное действие. Попробуйте снова.")
            print("-" *20)
    
    if not human.jizn():
        break
