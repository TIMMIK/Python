class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.ism}."
        return info
    def get_age(self,yil):
        """Shaxsni yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        # Функция super() используется для предоставления доступа к методам и свойствам родительского или родственного класса.
        # Функция super() возвращает объект, представляющий родительский класс.
        super().__init__(ism, familiya, passport, tyil) # копирует, перемешает или передает
        self.idraqam = idraqam
        self.bosqich = 1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

talaba1 = Talaba('Timur','Tursunov','Passport',2005,'idCode')
print(talaba1.get_id())
print(talaba1.get_bosqich())
print(talaba1.get_info())