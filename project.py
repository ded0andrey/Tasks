class Medicine:
    company_name = "Pharmacy"  # Статический атрибут - название компании
    medicines_count = 0  # Статический атрибут - количество лекарств

    def __init__(self, name, composition, dose, price):
        # Динамические атрибуты
        self.name = name
        self.composition = composition
        self.dose = dose
        self.price = price
        Medicine.medicines_count += 1  # Увеличиваем количество лекарств при создании нового экземпляра класса

    # динамический метод
    def display_info(self):
        print(f"Название: {self.name}\nСостав: {self.composition}\nДозировка: {self.dose}\nЦена: {self.price}") \

    @staticmethod  # статистический метод
    def get_company_name():
        return Medicine.company_name

    @classmethod
    def get_medicines_count(cls):
        return cls.medicines_count


med1 = Medicine("Аспирин", "Ацетилсалициловая кислота", "200 мг", 80)
med2 = Medicine("Но-шпа", "Дротаверин", "40 мг", 118)


med2.display_info()
print('Название компании:', Medicine.get_company_name())
print(Medicine.get_medicines_count())  # количество лекарств
