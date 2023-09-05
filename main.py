import json

class Cinema():
    "bu sinif kulaniciyi kaydeder"
    def __init__(self, name, surname, age, Email):
        self.name = name
        self.surname = surname
        self.age = age
        self.Email = Email

    def save(self):
        print(self.name,"isimli kişi kayıt edildi.")

    def show_info(self):
        print(self.name, self.surname, self.age, self.Email)

class Salon1(Cinema):
    def __init__(self, name, surname, age, Email):
        super().__init__(name,surname,age,Email)


c =  Cinema("Zübeyir", "Yilmaz", 15, "deneme@gmail.com")
c.save()
c.show_info()

with open("Cinema.json", "w") as f:
    json.dump(c.to_json(), f, indent=4)
