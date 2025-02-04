import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.happines = 100
        self.satiety = 100
        self.house = None
        self.job = None

    def housse(self, house):
        self.house = house
        
    def na_job(self, job):
        self.job = job

    def eat(self):
        if self.satiety < 100 and self.house.food > 0:
            self.satiety += 50  
            self.happines += 30 
            self.house.food -= 1
            print(f"{self.name} поел. Сытость: {self.satiety}, Счастье: {self.happines}")
        else:
            print(f"{self.name} не может поесть. Сытость: {self.satiety}, еда: {self.house.food}")
    
    def work(self):
        if self.job:
            self.money += self.job.salary
            self.happines -= self.job.happiness
            self.satiety -= 20
            print(f"{self.name} работал. Деньги: {self.money}, Счастье: {self.happines}, Сытость: {self.satiety}")
        else:
            print(f"У {self.name} нет работы.")
        
    def shop(self):
        print("-" *20)
        print(f"Добро пожаловать в магазин, {self.name}!")
        print("Что хотите купить?")
        print("1: Еда (20 денег 1 штука)")
        print("2: Выйти из магазина")
        
        while True:
            c = input("Введите действие: ")
            
            if c == "1":
                if self.money >= 20:
                    self.money -= 20
                    self.house.food += 1
                    print(f"{self.name} купил 1 ед. еды. Деньги: {self.money}, Еда в доме: {self.house.food}")
                    print("-" *20)
                elif self.money < 20:
                    print(f"У вас недостаточно денег для покупки еды.")
                    print("-" *20)
            elif c == "2":
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
        print(f"Имя {self.name}: Деньги: {self.money}, Счастье: {self.happines}, Сытость: {self.satiety}, Еда в доме: {self.house.food}")

class Job:
    def __init__(self, position, salary, happiness):
        self.position = position
        self.salary = salary
        self.happiness = happiness

class House:
    def __init__(self):
        self.food = 0

house = House()
job = Job("Gde to", 100, 20)
human = Human("Alexandr")
human.na_job(job)
human.housse(house)

vibor = {
    "1": human.eat,
    "2": human.work,
    "3": human.shop,
}

for day in range(1, 100):
    human.status()
    print(f"\nДень {day}:")
    print("Действие: ")
    print("1: Покушать")
    print("2: Работать")
    print("3: Магазин")
    
    while True:
        viborr = input("Введите действие: ")
        if viborr in vibor:
            vibor[viborr]()
            print("--------------------------")
            break
        else:
            print("Неверное действие. Попробуйте снова.")
            print("--------------------------")
    
    if not human.jizn():
        break