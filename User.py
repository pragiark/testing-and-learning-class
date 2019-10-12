class User():
    """Create user class"""
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Describe user - Print"""
        print("Użytkownik " + self.first_name + " " + self.last_name + " ma lat: " + str(self.age)
              + " mieszka w mieście: " + self.city)

    def increment_login_attempts(self):
        """"incremetnt login attempts"""
        self.login_attempts += 1

    def read_login_attempts(self):
        """Read login try"""
        print(str(self.login_attempts))

    def reset_login_attenpts(self):
        """Reset login attemps"""
        if self.login_attempts > 0:
            self.login_attempts = 0

class Admin(User):
    """"Class inferited"""
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["może dodać post", "może usunąć post"]

    def show_privileges(self):
        """Return admin privleges"""
        print(self.first_name + ", " + self.last_name + " ma uprawnienia do: ")
        for adm in self.privileges:
            print(adm)


paulina = User("Paulina", "Pragier", 32, "Gdynia")
paulina.describe_user()
paulina.read_login_attempts()
paulina.reset_login_attenpts()
paulina.read_login_attempts()
paulina.increment_login_attempts()
paulina.increment_login_attempts()
paulina.increment_login_attempts()
paulina.increment_login_attempts()
paulina.increment_login_attempts()
paulina.increment_login_attempts()
paulina.increment_login_attempts()
paulina.read_login_attempts()
paulina.reset_login_attenpts()
paulina.read_login_attempts()

arek = Admin("Arek", "Pragier", 38, "Gdynia")
arek.describe_user()
arek.show_privileges()