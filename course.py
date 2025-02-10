import random
# Человек
class Human:
    def __init__(self, name):
        self.name = name
        self.money = 10000000
        self.happines = 1000000
        self.satiety = 1000000
        self.house = None
        self.job = None
        self.repair_kits = 0
        self.fuel = 0
        self.car = None


    def housse(self, house):
        self.house = house

    def buy_car(self, car):
        self.car = car
        print(f"{self.name} теперь с машиной {self.car.brand}.")

    def na_job(self, job):
        self.job = job
    # Покушать
    def eat(self):
        print("1: Поесть еду")
        print("2: Поесть мороженое")
        a = input("Что хотите съесть?: ")
        # Поедание еды
        if a == "1" and self.house.food > 0:
            self.satiety += 20  
            self.happines += 10 
            self.house.food -= 1
        # Поедание мороженого
        elif a == "2" and self.house.ice_cream > 0:
            self.satiety += 5
            self.happines += 5
            self.house.ice_cream -= 1
        else:
            print(f"{self.name} не может поесть. Сытость: {self.satiety}, еда: {self.house.food}, мороженое: {self.house.ice_cream}")
    # Работа
    def work(self):
        if self.job:
            self.money += self.job.salary
            self.happines -= 20
            self.satiety -= 10
            print(f"{self.name} работал. Деньги: {self.money}, Счастье: {self.happines}, Сытость: {self.satiety}")
        else:
            print(f"У {self.name} нет работы.")
    # Магазин
    def shop(self):
        print("-" *20)
        print(f"Добро пожаловать в магазин, {self.name}!")
        print("Что хотите купить?")
        print("1: Купить еду (20 денег за 1 штуку)")
        print("2: Купить ремкомплект для машины (50 денег за 1 штуку)")
        print("3: Купить мороженое (10 денег за 1 штуку)")
        print("4: Купить топливо (100 денег за 20 литров)")
        print("5: Купить машину (1000 денег)")
        print("6: Выйти из магазина")
        
        while True:
            c = input("Введите действие: ")
            # Покупка еды
            if c == "1":
                # Проверка на наличие еды
                if self.house.food >= 10:
                    print(f"{self.name} не может купить еду, так как в доме уже есть больше 10 еды.")
                    print("-" *20)
                    # Проверка на наличие денег
                elif self.money >= 20:
                    self.money -= 20
                    self.house.food += 1
                    self.satiety -= 10
                    print(f"{self.name} купил 1 ед. еды. Деньги: {self.money}, Еда в доме: {self.house.food}")
                    print("-" *20)
                else:
                    print(f"У вас недостаточно денег для покупки еды.")
                    print("-" *20)
            # Покупка ремкомплекта
            elif c == "2":
                # Проверка на наличие ремкомплекта
                if self.repair_kits >= 1:
                    print(f"{self.name} не может купить ремкомплект, так как у него уже есть больше одного.")
                    print("-" * 20)
                    # Проверка на наличие денег
                elif self.money >= 50:
                        self.money -= 50
                        self.satiety -= 10
                        self.repair_kits += 1  
                        print(f"{self.name} купил 1 ед. ремкомплекта. Деньги: {self.money}, Ремкомплектов на руках: {self.repair_kits}")
                        print("-" * 20)
                else:
                    print(f"У вас недостаточно денег для покупки ремкомплекта.")
                    print("-" * 20)
            # Покупка мороженого
            elif c == "3":
                #   Проверка на наличие мороженого
                if self.house.ice_cream >= 10:
                    print(f"{self.name} не может купить мороженое, так как в доме уже есть больше 10 мороженого.")
                    print("-" *20)
                elif self.money >= 10:
                    self.money -= 10
                    self.house.ice_cream += 1
                    self.satiety -= 5
                    print(f"{self.name} купил 1 ед. мороженого. Деньги: {self.money}, Мороженое в доме: {self.house.ice_cream}")
                    print("-" *20)
                else:
                    print(f"У вас недостаточно денег для покупки мороженого.")
                    print("-" *20)
            # Покупка топлива
            elif c == "4":
                # Проверка на наличие топлива
                if self.car.fuel >= 100:
                    print(f"{self.name} не может купить топливо, так как у него уже есть больше 100 литров.")
                    print("-" *20)
                elif self.money >= 100:
                    self.money -= 100
                    self.car.fuel += 20
                    self.satiety -= 10
                    print(f"{self.name} купил 20 литров топлива. Деньги: {self.money}, Топливо: {self.car.fuel}")
                    print("-" *20)
                else:
                    print(f"У вас недостаточно денег для покупки топлива.")
                    print("-" *20)
            # Покупка машины
            elif c == "5":
                if self.car:
                    print(f"{self.name} не может купить машину, так как у него уже есть машина.")
                    print("-" *20)
                elif self.money >= 1000:
                    self.money -= 1000
                    self.buy_car(car)
                    print(f"{self.name} купил машину. Деньги: {self.money}")
                    print("-" *20)
                else:
                    print(f"У вас недостаточно денег для покупки машины.")
                    print("-" *20)

            # Выход из магазина
            elif c == "6":
                print(f"{self.name} покинул магазин.")
                print("-" *20)
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
                print("-" *20)
                            
    # Проверка на жизнь
    def jizn(self):
        if self.satiety <= 0 or self.happines <= 0:
            print(f"{self.name} не смог выжить.")
            return False
        return True
    # Уборка
    def clean(self):
        if self.house:
            self.house.mess = 0
            self.happines += 5
            print(f"{self.name} убрался в доме. Счастье: {self.happines}")
        else:
            print(f"У {self.name} нет дома для уборки.")
    # Статус
    def status(self):
        print(f"Имя {self.name}: Деньги: {self.money}, Счастье: {self.happines}, Сытость: {self.satiety}, Еда в доме: {self.house.food}, Ремкомплекты: {self.repair_kits}")

        # Машина
class Auto(Human):
    def __init__(self, brand, fuel, durability, fuel_consumption):
        self.brand = brand
        self.fuel = fuel 
        self.durability = durability
        self.fuel_consumption = fuel_consumption
    # Движение
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
    def __init__(self, status, salary):
        self.status = status
        self.salary = salary

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.ice_cream = 0
    def house_status(self):
        print(f"Беспорядок: {self.mess}, Еда: {self.food}, Мороженок дома: {self.ice_cream}")


car = Auto("Toyota", 0, 100, 5)  
house = House()
job = Job("Programmer", 100)
human = Human("Alexandr")
human.buy_car(car)
human.na_job(job)
human.housse(house)

vibor = {
    "1": human.eat,
    "2": human.work,
    "3": human.shop,
    "4": car.car_status,  
    "5": car.move,
    "6": car.repair,  
    "7": human.clean,
    "8": house.house_status
}

for day in range(1, 100):
    house.mess += random.randint(0, 5)
    human.status()
    print(f"День {day}:")
    print("Действие: ")
    print("1: Покушать")
    print("2: Работать")
    print("3: Магазин")
    print("4: Статус машины")
    print("5: Поездить на машине")
    print("6: Починить машину")
    print("7: Уборка")
    print("8: Статус дома")
    
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