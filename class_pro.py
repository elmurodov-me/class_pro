class Girls:
    def money(self):print("give me money, i will give you honey!")
    def walk(self):print("if you wanna for me walk with me!")
    def beautiful(self):print("No all girls are beatiful")
    def figure(self):print("90 60 90")

class Boys:
    def walk(self):print("if girls give honey ,boys get walk")
    def figure(self):print("need not")
    def money(self):print("if boys have a money, they have a honey")
    def dialog(self):print("if girl have a figure 90 60 90 boys begin the dialog")

def main():
    guzal = Girls()
    Anvar = Boys()
    in_the_xotira_maydoni(guzal)
    in_the_xadra_maydoni(Anvar)

def in_the_xotira_maydoni(xusnida):
    xusnida.money()
    xusnida.walk()
def in_the_xadra_maydoni(guzal):
    guzal.dialog()
    guzal.figure()

if __name__=="__main__":main()