import colorama 
import os
import pyfiglet
import webbrowser

print(colorama.Fore.GREEN + "")
print(pyfiglet.figlet_format("Moon's Player", font = "big"))
print(colorama.Fore.WHITE + "")

def menu():
    print("       1) Play                                      2) Exit")

menu()
option = int(input(">>>> "))

while option != 0:
    if option == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print(colorama.Fore.GREEN + "")
        print(pyfiglet.figlet_format("Which Artist?", font = "big"))
        print(colorama.Fore.WHITE + "")

        def menu():
            print(colorama.Fore.RED+"      1)MoonHf               2)Rory in early 20s")
            print(colorama.Fore.WHITE + "")
        menu()
        option = int(input(">>>> "))
        

        if option == 1:
            os.system("cls" if os.name == "nt" else "clear")
            print(colorama.Fore.GREEN + "")
            print(pyfiglet.figlet_format("Chose a song ", font = "big"))
            print(colorama.Fore.WHITE + "")
            def menu():
                print("1) Im atheist")
                print("2) Shame me")
                print("99) Soundcloud profile")
            menu()
            option = int(input(">>>> "))
            if option == 1:
                url='https://soundcloud.com/moonhff/im-atheist?si=74cb07ca001e4187886a942610abda88&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                webbrowser.open_new_tab(url)    
            if option == 2:
                 url='https://soundcloud.com/moonhff/shame-me?si=e3a4060157964e068b5b69e93d176843&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                 webbrowser.open_new_tab(url)
            if option == 99:
                url='https://soundcloud.com/moonhff'
                webbrowser.open_new_tab(url)
        if option == 2:
            os.system("cls" if os.name == "nt" else "clear")
            print(colorama.Fore.GREEN + "")
            print(pyfiglet.figlet_format("Chose a song ", font = "big"))
            print(colorama.Fore.WHITE + "")
            def menu():
                print("1)forgotten notes")
                print("2)Tayru Mu")
                print("3)no need to worry_no need to worry")
                print("4)幻影")
                print("5)Tokomori Pasuu")
                print("6)Digital winter v3")
                print("99) Soundcloud profile")
            menu()
            option = int(input(">>>> "))
            if option ==1:
                url='https://soundcloud.com/rorynearly20s/forgotten-notes?si=84f6e6d5454b4234aef92a21faa72791&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                webbrowser.open_new_tab(url)
            if option ==2:
                url='https://soundcloud.com/rorynearly20s/tayru-mu?si=1a08871effdb4012816b38aa40740942&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                webbrowser.open_new_tab(url)
            if option ==3:
                url='https://soundcloud.com/rorynearly20s/no-need-to-worry_no-need-to-worry?si=5ef03dd090c04fc297e1504bbcbf6909&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                webbrowser.open_new_tab(url)
            if option ==4:
                url='https://soundcloud.com/rorynearly20s/avf0hsdtptce?si=901f277bc00f40deb6cc273c1c25241a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                webbrowser.open_new_tab(url)
            if option ==5:
                url='https://soundcloud.com/rorynearly20s/tokomori-pasuu?si=ee8e840d9db2419a81a0d9946fdc1c87&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                webbrowser.open_new_tab(url)
            if option ==6:
                url='https://soundcloud.com/rorynearly20s/digital-winter-v3?si=98026a50ecd14ba98df1ff2fa04a3813&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
                webbrowser.open_new_tab(url)
            if option ==99:
                url='https://soundcloud.com/rorynearly20s'
                webbrowser.open_new_tab(url)
    elif option == 2:
        os.system("cls" if os.name == "nt" else "clear")
        print(colorama.Fore.RED+"Bye")
        exit()