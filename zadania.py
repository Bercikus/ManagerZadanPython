
#uzyto polecenia   'python -m pydoc -w'   w celu utworzenia dokumentacju


#zadanie1
from datetime import datetime
import json
import time
import os

def pomiarCzasuFunkcji(funkcja): 
    def wzbogaconaFunkcja(*args, **kwargs):
        start_time = time.time()
        result = funkcja(*args, **kwargs)
        end_time = time.time()
        czas_wykonania = end_time - start_time
        print(f"Funkcja '{funkcja.__name__}' wykonana w czasie: {czas_wykonania:.4f} sekund")
        os.system('pause')
        return result
    return wzbogaconaFunkcja




class Zadanie:
    """
    Reprezentuje pojedyncze zadanie.

    :param tytul: Tytuł zadania.
    :param opis: Opis zadania.
    :param termin: Termin wykonania zadania.
    :param wykonane: Flaga określająca, czy zadanie zostało wykonane.
    """
    def __init__(self, tytul, opis, termin, wykonane):
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania =termin
        self.wykonane = wykonane

   
    def __str__(self):
        """
        Zwraca reprezentację tekstową zadania.

        :return: Opis zadania w formacie tekstowym.
        """
        czyWykonano = "wykonane" if self.wykonane else "niewykonane"
        result =  f"Zadanie: {self.tytul}\nOpis: {self.opis}\nTermin: {self.termin_wykonania}\nStatus: {czyWykonano}"
         
         # Wyświetlanie dodatkowych atrybutów
         #tworzenie listy o wskazanym formacie
        extra_attributes = [f"{key}: {value}" for key, value in self.__dict__.items() if key not in ("tytul", "opis", "termin_wykonania", "wykonane")]
        if extra_attributes:
            result += "\n" + "\n".join(extra_attributes)
        return result

class ZadaniePriorytetowe(Zadanie):
    """
    Reprezentuje zadanie priorytetowe.

    :param tytul: Tytuł zadania.
    :param opis: Opis zadania.
    :param termin: Termin wykonania zadania.
    :param wykonane: Flaga określająca, czy zadanie zostało wykonane.
    :param priorytet: Poziom priorytetu zadania.
    """
    def __init__(self, tytul, opis, termin, wykonane, priorytet):
        super().__init__(tytul, opis, termin, wykonane)
        self.priorytet = priorytet

    def __str__(self):
        """
        Zwraca reprezentację tekstową zadania priorytetowego.

        :return: Opis zadania priorytetowego w formacie tekstowym.
        """
        baseSTR = super().__str__()
        return baseSTR + f"\nPriorytet: {self.priorytet}"

class ZadanieRegularne(Zadanie):
    """
    Reprezentuje zadanie regularne.

    :param tytul: Tytuł zadania.
    :param opis: Opis zadania.
    :param termin: Termin wykonania zadania.
    :param wykonane: Flaga określająca, czy zadanie zostało wykonane.
    :param powtarzalnosc: Opis powtarzalności zadania.
    """
    def __init__(self, tytul, opis, termin, wykonane, powtarzalnosc):
        super().__init__(tytul, opis, termin, wykonane)
        self.powtarzalnosc = powtarzalnosc
    
    def __str__(self):
        """
        Zwraca reprezentację tekstową zadania regularnego.

        :return: Opis zadania regularnego w formacie tekstowym.
        """
        baseSTR = super().__str__()
        return baseSTR + f"\nPowtarzalnosc: {self.powtarzalnosc}"   









class ManagerZadan:
    """
    Klasa do zarządzania listą zadań.

    Oferuje metody do dodawania, usuwania, edytowania oraz zapisywania zadań.
    """

    def __init__(self):
        self.zadania = [] 

    def dodajZadanie(self, zadanie):
        """
        Dodaje nowe zadanie do listy.

        :param zadanie: Obiekt zadania do dodania.
        """
        self.zadania.append(zadanie)

#Domyślny argument
    def usunZadanie(self, indeks = 0):
        """
        Usuwa zadanie z listy na podstawie podanego indeksu.

        :param indeks: Indeks zadania do usunięcia. Domyślnie 0.
        """
        if len( self.zadania) > indeks and indeks >=0:
            self.zadania.pop(indeks)

#Domyślny argument
    def edytujZadanie(self, indeks, tytul=None, opis=None, termin=None, wykonane=None, priorytet=None, powtarzalnosc=None):
        """
        Edytuje istniejące zadanie.

        :param indeks: Indeks zadania do edycji.
        :param tytul: Nowy tytuł zadania (opcjonalne).
        :param opis: Nowy opis zadania (opcjonalne).
        :param termin: Nowy termin wykonania (opcjonalne).
        :param wykonane: Nowy status wykonania (opcjonalne).
        :param priorytet: Nowy priorytet (opcjonalne).
        :param powtarzalnosc: Nowa powtarzalność (opcjonalne).
        """
        if 0 <= indeks < len(self.zadania):
            zadanie = self.zadania[indeks]
            
            if tytul is not None:
                zadanie.tytul = tytul
            if opis is not None:
                zadanie.opis = opis
            if termin is not None:
                zadanie.termin_wykonania = termin
            if wykonane is not None:
                zadanie.wykonane = wykonane

            # Sprawdzenie, czy zadanie ma dodatkowe atrybuty
            if isinstance(zadanie, ZadaniePriorytetowe) and priorytet is not None:
                zadanie.priorytet = priorytet
            if isinstance(zadanie, ZadanieRegularne) and powtarzalnosc is not None:
                zadanie.powtarzalnosc = powtarzalnosc
            
            print(f"Zadanie o indeksie {indeks} zostało zaktualizowane.")
        else:
            print(f"Błąd: Indeks {indeks} jest poza zakresem.")

    def oznaczZadanie(self, indeks, value = True):
        """
        Oznacza zadanie jako wykonane lub niewykonane.

        :param indeks: Indeks zadania, które ma być oznaczone.
        :param value: Flaga, która określa, czy zadanie ma być oznaczone jako wykonane (domyślnie True).
        """
        self.zadania[indeks].wykonane = value
    

    def pokazListeZadan(self):
        """
        Wyświetla listę wszystkich zadań w menedżerze.

        Zadania są wypisywane na ekranie w kolejności, w jakiej są przechowywane w liście.
        """
        n = 1
        for zadanie in self.zadania:
            print(f"\n[{n}]=============================================================")
            print(zadanie)
            n = n+1

    def __contains__(self, zadanie): 
            """
            Sprawdza, czy dane zadanie znajduje się w liście zadań.

            :param zadanie: Zadanie do sprawdzenia.
            :return: True, jeśli zadanie znajduje się w liście, w przeciwnym razie False.
            """
            return zadanie in self.zadania

    def parse_date(self, date_string):
        """
        Parsuje podany ciąg znaków reprezentujący datę do obiektu datetime.

        Obsługuje różne formaty daty. Jeśli żaden format nie pasuje, zwraca None.

        :param date_string: Ciąg znaków reprezentujący datę.
        :return: Obiekt datetime, jeśli parsowanie się powiodło, w przeciwnym razie None.
        """
        
        # Lista akceptowanych formatów daty
        date_formats = ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]
        for date_format in date_formats:
            try:
                return datetime.strptime(date_string, date_format)
            except ValueError:
                continue 
        return None

    @pomiarCzasuFunkcji
    def sortujZadania(self): 
        """
        Sortuje listę zadań według terminu wykonania.

        Zadania są sortowane w kolejności rosnącej na podstawie daty wykonania.
        Używa dekoratora pomiarCzasuFunkcji do pomiaru czasu wykonania metody.
        """
        self.zadania.sort(key=lambda zadanie: self.parse_date(zadanie.termin_wykonania) or datetime.max) 
 
    @pomiarCzasuFunkcji
    def zapiszZadaniaDoPliku(self, nazwa_pliku):
        """
        Zapisuje listę zadań do pliku JSON.

        Konwertuje zadania na listę słowników, które są zapisywane w formacie JSON.

        :param nazwa_pliku: Nazwa pliku, do którego zapisane zostaną zadania.
        """

        # Konwersja listy zadań na listę słowników, która będzie zapisywana do pliku
        zadania_data = []
        for zadanie in self.zadania:
            zadanie_dict = {
                "tytul": zadanie.tytul,
                "opis": zadanie.opis,
                "termin_wykonania": zadanie.termin_wykonania,
                "wykonane": zadanie.wykonane
            }
            
            # Dodanie dodatkowych atrybutów specyficznych dla klasy zadania
            if isinstance(zadanie, ZadaniePriorytetowe):
                zadanie_dict["typ"] = "priorytetowe"
                zadanie_dict["priorytet"] = zadanie.priorytet
            elif isinstance(zadanie, ZadanieRegularne):
                zadanie_dict["typ"] = "regularne"
                zadanie_dict["powtarzalnosc"] = zadanie.powtarzalnosc
            else:
                zadanie_dict["typ"] = "zwykle"
            
            zadania_data.append(zadanie_dict)
        
        # Zapis do pliku JSON
        with open(nazwa_pliku, 'w', encoding='utf-8') as file:
            json.dump(zadania_data, file, ensure_ascii=False, indent=4)
        print(f"Zadania zapisano do pliku {nazwa_pliku}.")

    @pomiarCzasuFunkcji
    def odczytajZadaniaZPliku(self, nazwa_pliku):
        """
        Wczytuje zadania z pliku JSON.

        Usuwa istniejące zadania i wczytuje nowe z pliku.

        :param nazwa_pliku: Nazwa pliku, z którego mają być wczytane zadania.
        :raises FileNotFoundError: Jeśli plik nie istnieje.
        :raises json.JSONDecodeError: Jeśli plik nie zawiera prawidłowych danych JSON.
        """
        # Wczytanie danych z pliku JSON
        try:
            with open(nazwa_pliku, 'r', encoding='utf-8') as file:
                zadania_data = json.load(file)
            
            # Oczyszczenie listy zadań przed wczytaniem nowych
            self.zadania.clear()
            
            for zadanie_dict in zadania_data:
                tytul = zadanie_dict["tytul"]
                opis = zadanie_dict["opis"]
                termin = zadanie_dict["termin_wykonania"]
                wykonane = zadanie_dict["wykonane"]
                typ = zadanie_dict.get("typ", "zwykle")
                
                # Tworzenie odpowiedniego obiektu na podstawie typu zadania
                if typ == "priorytetowe":
                    priorytet = zadanie_dict.get("priorytet", "")
                    zadanie = ZadaniePriorytetowe(tytul, opis, termin, wykonane, priorytet)
                elif typ == "regularne":
                    powtarzalnosc = zadanie_dict.get("powtarzalnosc", "")
                    zadanie = ZadanieRegularne(tytul, opis, termin, wykonane, powtarzalnosc)
                else:
                    zadanie = Zadanie(tytul, opis, termin, wykonane)
                
                # Dodanie zadania do listy zadań
                self.dodajZadanie(zadanie)
            print(f"Zadania wczytano z pliku {nazwa_pliku}.")
        
        except FileNotFoundError:
            print(f"Błąd: Plik {nazwa_pliku} nie istnieje.")
        except json.JSONDecodeError:
            print(f"Błąd: Plik {nazwa_pliku} nie zawiera prawidłowych danych JSON.")

    def dodajDodatkoweInformacje(self, indeks, **kwargs):
        """
        Dodaje dodatkowe informacje do istniejącego zadania.

        :param indeks: Indeks zadania, do którego dodawane są dodatkowe informacje.
        :param kwargs: Dodatkowe informacje w postaci par klucz-wartość.
        """
        if 0 <= indeks < len(self.zadania):
            zadanie = self.zadania[indeks]
            for key, value in kwargs.items():
                setattr(zadanie, key, value)      
        


