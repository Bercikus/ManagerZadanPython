from zadania import *
import os

def str_to_bool(value):
    return value.lower() in ("yes", "true", "t", "1","tak", "y")

def pokazMenu():
    print("========================================================")
    print("======================|MENU|============================")
    print("========================================================")
    print(" 1. Dodaj")
    print(" 2. Usun")
    print(" 3. Oznacz")
    print(" 4. Edytuj")
    print(" 5. Sortuj wedlug terminu") 
    print(" 6. Zapisz zadania do pliku") 
    print(" 7. Odczytaj zadania z pliku") 
    print(" 8. Dodaj dodatkowe informacje do zadania") 
    print(" 9. Wyjdz")

choose = 0
manager = ManagerZadan()

while choose !="9": 
    print("                   Lista Zadan")
    if manager.zadania.__len__() == 0:
        print(" (brak zadan)")
    manager.pokazListeZadan() 
    pokazMenu() 
    choose = input(">")
    if choose == "1":
        os.system("cls")
        print("=========== Kreator zadan ===========")
        tytul = input("Tytuł: ")
        opis = input("Opis: ")
        termin = input("Termin: ")
        czyWykonane = str_to_bool(input("Czy zadanie wykonane(tak/nie): "))
        typ = "" 
        while typ not in ("p", "r", "z"):
            typ = input("Czy zadanie priorytetowe (p) regularne (r) zwykłe (z): ")
        zadanie = None
        if typ == "p":
            priorytet = input("Priorytet: ")
            zadanie = ZadaniePriorytetowe(tytul, opis, termin, czyWykonane, priorytet) 
        elif typ == "r":
            powtarzalnosc = input("Powtarzalność: ")
            zadanie = ZadanieRegularne(tytul, opis, termin, czyWykonane, powtarzalnosc)
        elif typ == "z":
            zadanie = Zadanie(tytul, opis, termin, czyWykonane)
        manager.dodajZadanie(zadanie)
    elif choose == "2":
        indeks = int(input("Numer zadania do usuniecia: ")) -1
        if indeks>=0 and indeks<manager.zadania.__len__():
             manager.usunZadanie(indeks)
    elif choose == "3":
        indeks = int(input("Numer zadania do oznaczenia: ")) -1
        if indeks>=0 and indeks<manager.zadania.__len__():
            czyWykonane = str_to_bool(input("Czy zadanie wykonane(tak/nie): "))
            manager.oznaczZadanie(indeks, czyWykonane)
    elif choose == "4":
        indeks = int(input("Numer zadania do edycji: ")) -1
        if indeks>=0 and indeks<manager.zadania.__len__():
            print("Jeśli chcesz pominąć wprowadzenie pola, nacisnij enter") 
            tytul = input("Nowy tytuł: ")
            opis = input("Nowy opis: ")
            termin = input("Nowy termin wykonania: ")
            wykonane = input("Czy zadanie wykonane (tak/nie): ")
            priorytet = ""
            powtarzalnosc = ""
            if isinstance(manager.zadania[indeks], ZadaniePriorytetowe):
                priorytet = input("Nowy priorytet: ")
            elif isinstance(manager.zadania[indeks], ZadanieRegularne):
                powtarzalnosc = input("Nowa powtarzalność: ")

            # Konwersja pustych pól na None - odrzucenie nie zedytowanych pól
            tytul = tytul if tytul else None
            opis = opis if opis else None
            termin = termin if termin else None
            wykonane = True if wykonane.lower() == "tak" else False if wykonane.lower() == "nie" else None
            priorytet = priorytet if priorytet else None
            powtarzalnosc = powtarzalnosc if powtarzalnosc else None
            
            manager.edytujZadanie(indeks, tytul, opis,termin,wykonane,priorytet,powtarzalnosc)
    elif choose == "5":
        manager.sortujZadania()
        print("Posortowano")
    elif choose == "6":
        print("Zapis do pliku")
        file_name = input("Podaj nazwę pliku do ktorego chcesz zapisac zadania: ")
        file_name += ".txt"
        manager.zapiszZadaniaDoPliku(file_name) 
    elif choose == "7":
        print("Odczyt z pliku")
        file_name = input("Podaj nazwę pliku z ktorego chcesz odczytac zadania: ")
        file_name += ".txt"
        manager.odczytajZadaniaZPliku(file_name)
    elif choose == "8":
        indeks = int(input("Numer zadania do którego chcesz dodać dodatkowe informacje: ")) -1
        if indeks>=0 and indeks<manager.zadania.__len__():
            collection={}
            print("Dodawanie dodatkowych informacji do zadania.") 
            while True:
                klucz = input("Podaj nazwę dodatkowej informacji (lub 'q', aby zakończyć): ")
                if klucz.lower() == 'q':
                    break
                wartosc = input(f"Podaj wartość dla '{klucz}': ")
                collection[klucz] = wartosc
            manager.dodajDodatkoweInformacje(indeks, **collection)
            
            






print("Koniec programu")

 











print("\n\n\n__________________________")


























