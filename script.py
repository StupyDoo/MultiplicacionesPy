import random
import winsound
import time
import math

record = 0
timeElapsed = 0


def start_chronometer():
    global timeElapsed
    timeElapsed = time.time()


def stop_chronometer():
    global timeElapsed
    timeElapsed = time.time() - timeElapsed
    print("\nTiempo transcurrido: " +
          "{:.3f}".format(timeElapsed) + " segundos")


def beep(result):
    if result == "bien":
        winsound.Beep(700, 200)
    elif result == "mal":
        winsound.Beep(200, 100)
        winsound.Beep(200, 100)
    elif result == "record":
        winsound.Beep(1000, 200)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 200)


def main():
    while True:
        test()


def read_file():
    # if the file doesn't exist, create it
    try:
        file = open("score.txt", "r")
        score = file.read()
        file.close()
    except FileNotFoundError:
        file = open("score.txt", "w")
        file.write("0")
        file.close()
        score = 0
    return score


def test():
    print("\nResuelve las siguientes operaciones en el menor tiempo posible")
    score = read_file()
    print("Record: " + str(score))

    input("\033[1;37m" + "\nPresiona Enter para continuar\n" + "\033[0m")
    start_chronometer()
    total = 10
    score = 0
    for i in range(1, total+1):
        x = random.randint(3, 9)
        y = random.randint(3, 9)
        resultado = input(str(x) + " x " + str(y) + " = ")

        if (resultado != "" and int(resultado) == (x * y)):
            score += 1
            # print green font
            print("\033[1;32m" + "¡Correcto!" + "\033[0m")
            beep("bien")
        else:
            # print red font
            print("\033[1;32m" + str(x) + " x " +
                  str(y) + " = " + str(x*y) + "\033[0m")
            print("\033[1;31m" + "Incorrecto" + "\033[0m")
            beep("mal")

    stop_chronometer()
    print("Respuestas correctas: " + str(score) + "/" + str(total))
    score = int(score / timeElapsed * 100)
    print("Tu puntuación es: " + str(score).zfill(0))
    input("\033[1;37m" + "\nPresiona Enter para continuar\n" + "\033[0m")
    create_file(score)


def create_file(score):
    file = open("score.txt", "r+")
    oldScore = 0

    try:
        oldScore = int(file.read())
    except:
        file.write(str(oldScore))

    if (score > oldScore):
        # clear the file
        file.seek(0)
        file.truncate()
        file.write(str(score))
        # print yellow font
        print("\033[1;33m" + "Nuevo record: " + str(score) + "\033[0m")
        beep("record")
    file.close()


# create the main function contructor
if __name__ == "__main__":
    main()

# print blod font python
#
