import sys
import winsound
Freq = 2500
Dur = 900
winsound.Beep(Freq,Dur)
print("Hello world")
print("You who?")
laungage = input("You Russian or English?: ")
if laungage == "English":
    print("Hello")
    namme = input("What's your name? ")
    print("Hi " + namme + " good day ")
    print("""This is a list of what you can find out about, just write a number and you will find out 
    1.Yandex
    2.Google
    3.Discord
    4.Malwarebytes
    5.Vivaldi
    6.Brave
    7.Steam
    8.AnyDesk
    """)
    print("please write ---help")
    while True:
        noww = input("What are we going to do or find out now? ")
        if noww == "1.":
            print("Yandex is a Russian company that created Yandex browser and many other services.")
        elif noww == "2.":
            print("Google is the most popular company in the world and the most profitable. Also known for the massive Google Chrome browser that brought super changes to the world!")
        elif noww == "3.":
            print("This program is designed to communicate like Skype.")
        elif noww == "4.":
            print("Malwarebytes is an antivirus and in my humble opinion it is the best antivirus")
        elif noww == "5.":
            print("Vivaldi is almost an opera browser. When one developer left the opera company he wanted to create his own browser and created Vivaldi!")
        elif noww == "6.":
            print("Brave is a popular browser. It is like chrome and a fox muff. And it is fast as vivaldi and does not use all resources.")
        elif noww == "7.":
            print("Steam is an online service for the digital distribution of computer games and software developed and maintained by Valve.")
        elif noww == "8.":
            print("AnyDesk is a program written in c ++ and also that would remotely control a computer or help a person. I recommend to everyone!")
        elif noww == "---help":
            print("List")
            print("quit is for quit")
        elif noww == "quit":
            sys.exit()
        else:
            print("There is no such command")                
name = input("Как тебя зовут? ")
print(" Привет " + name + " Добрый день ")
print("""Это список о чём можно узнать просто напиши цифру и ты узнаешь 
    1.Яндекс
    2.Гугл
    3.Дискорд
    4.Malwarebytes
    5.Vivaldi
    6.Brave
    7.Steam
    8.AnyDesk
    """)
print("Напиши --help для подробности")    
while True:
    now = input("Что сейчас будем делать или узнавать? ")
    if now == "1":
      print("Яндекс - Русская Компания которая создала Яндекс браузер и многие другие сервисы.")
    elif now == "2":
        print("Это.")
        print("""
        Google — Это самая популярная компания в мире и самая доходная.Так же известна из за крупного браузера Google Chrome который принёс супер изменения в мире! 
        """)
    elif now == "3":
        print("Это программа создана для общения как скайп.")
    elif now == "4":
        print("Malwarebytes это антивирус и по моему скромному мнению это лучший антивирус")
    elif now == "5":
        print("Vivaldi браузер почти оперы.Когда один разработчик ушёл из компании opera то он захотел свой браузер создать и создал Vivaldi!")         
    elif now == "6":
        print("Brave это браузер популярен.Он как хром и мазила лиса.И он быстрый как вивалди и мало использует все ресурсы)")
    elif now == "7":
        print("Steam — онлайн-сервис цифрового распространения компьютерных игр и программ, разработанный и поддерживаемый компанией Valve.")
    elif now == "8":
        print("AnyDesk это программа написанная на c++ и так же что бы удаленно управлять компьютером или помогать человеку.Рекомендую всем!")
    elif now == "--help":
        print("Список")
        print("exit - это для выхода")
    elif now == "nerbi":
        print("Нерби спасибо огромное тебе так как я знаю то что ты читаешь!Ты самый лучший мой друг!Скоро тебе дам гта 5)))")    
    elif now == "exit":
        sys.exit()
    else:
        print("Нет такой команды")    