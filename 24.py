
#request input from user
def main():
    satu, dua, tiga, empat = get_input()
    calculations = Calculations(satu, dua, tiga, empat)
    calculations.add_all()

def get_input():
    confirm = "N"
    while confirm == "N":
        satu = int(input("Enter the first number: "))
        while satu < 1 or satu > 10:
            print("Please enter a number in range 1 to 10!")
            satu = int(input("Enter the first number: "))
        dua = int(input("Enter the second number: "))
        while dua < 1 or dua > 10:
            print("Please enter a number in range 1 to 10!")
            dua = int(input("Enter the second number: "))
        tiga = int(input("Enter the third number: "))
        while tiga < 1 or tiga > 10:
            print("Please enter a number in range 1 to 10!")
            tiga = int(input("Enter the third number: "))
        empat = int(input("Enter the fourth number: "))
        while empat < 1 or empat > 10:
            print("Please enter a number in range 1 to 10!")
            empat = int(input("Enter the fourth number: "))

        print("First: ", satu,
              "\nSecond: ", dua,
              "\nThird: ", tiga,
              "\nFourth: ", empat)
        confirm = input("Confirm(Y/N)? ")
        confirm = confirm[0].capitalize()

    return satu, dua, tiga, empat

#object-oriented public class Calculations, to calculate the user input
class Calculations():
    def __init__(self, satu, dua, tiga, empat):       #initialize private variables satu, dua, tiga, empat
        self.__satu = satu
        self.__dua = dua
        self.__tiga = tiga
        self.__empat = empat

    def set_satu(self, satu):                          #mutator method for variables
        self.__satu = satu

    def set_dua(self, dua):
        self.__dua = dua

    def set_tiga(self, tiga):
        self.__tiga = tiga

    def set_empat(self, empat):
        self.__empat = empat

    def get_satu(self):                               #accessor method for variables
        return self.__satu

    def get_dua(self):
        return self.__dua

    def get_tiga(self):
        return self.__tiga

    def get_empat(self):
        return self.__empat

    def add_all(self):
        solution = False
        if self.__satu + self.__dua + self.__tiga + self.__empat == 24:
            solution = True
            print("add em all")
            print(solution)
            return solution
        else:
            solution = False
            print(solution)
            return solution

    def add(self, a, b):
        result = a + b
        return result

    def subtract(self, a, b):
        result = a - b
        return result

    def multiply(self, a, b):
        result = a - b
        return result

    def divide(self, a, b):
        result = a/b
        return result



main()