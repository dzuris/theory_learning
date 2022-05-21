"""
-----------------------------------------------------------
@project: Theory learning
@file: theory_learning.py
@author: Adam Dzurilla
-----------------------------------------------------------
"""

import random
import os
import sys


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return "   "


def print_help_message():
    print("Usage:")
    print("\tpython3.8 theory_learning.py FILE")
    print()
    print("Choices:")
    print("\tr - random question")
    print("\ta - show answer")
    print("\tc | count - number of questions")
    print("\tall - print all questions")
    print("\th | help - print this message")
    print("\tquit - quit")
    print()
    print("This is help message for the program \"theory_learning.py\"")


class Subject:
    list_of_quest_and_answer = None
    value = None

    def __init__(self, input_file):
        # self.list_of_quest_and_answer = list_of_q_a
        self.load_from_file(input_file)

    def load_from_file(self, input_file):
        pass

    def select_random(self):
        self.value = random.choice(list(self.list_of_quest_and_answer))

    def print_ran_choice(self):
        self.select_random()
        print(self.value)

    def print_answer(self):
        if self.value is not None:
            print(self.list_of_quest_and_answer[self.value])

    def print_count(self):
        print(len(self.list_of_quest_and_answer))

    def print_all(self):
        num = 1
        for key in self.list_of_quest_and_answer:
            print(str(num) + ":\t" + key)
            num += 1


if __name__ == "__main__":
    list_ids = {"Domena": "Pomenovana mnozina skalarnych hodnot urciteho typu",
                "Skalarna hodnota": "Najmensia semanticka hodnota dat",
                "zlozena domena": "Domena zlozena z niekolkych jednoduchych domen",
                "relacia": "Dvojica (schema relacie, telo)",
                "stupen relacie": "Pocet atributov relacie",
                "kardinalita relacie": "m = | R* |",
                "kandidatny kluc": "Jednoznacne identifikuje n-ticu v relacii",
                "referencna integrita": "Sulad hodnot PK a FK predstavuje vztahy medzi riadkami tabuliek",
                "algebra matematicky": "Dvojica (domena, mnozina operacii)",
                "relacia matematicky": "podmnozina kartezskeho sucinu",
                "relacna algebra": "Dvojica (R, O)\nR - mnozina relacii\nO - mnozina operacii"
                                   "\n\t- tracidne mnozinove operacie (zjednotenie, prienik...)"
                                   "\n\t- specialne relacne operacie (projekcia, selekcia...)",
                "zjednotenie tabuliek": "UNION",
                "projekcia": "SELECT",
                "selekcia": "WHERE",
                "spojenie": "JOIN",
                "normalizacia": "2.vyznamna teoreticka podpora relacnych databazi",
                "3 typy zavislosti normalizacia": "1. funkcna zavislost"
                                                  "\n2. viachodnotove zavislosti"
                                                  "\n3. zavislosti na spojenie",
                "normalizacia - zachovanie zavislosti": "Vsetky povodne zavislosti musia byt zachovane a "
                                                        "lahko kontrolovatelne",
                "1NF": "Vsetky jej jednoduche domeny obsahuju iba atomicke hodnoty",
                "2NF": "Musi byt v 1NF a kazdy jej neklucovy atributy je plne funkcne "
                       "zavisly na kazdom kandidatnom kluci",
                "3NF": "Musi byt v 2NF a neexistuje ziadny neklucovy atribut, ktory je "
                       "tranzitivne zavisli na niektorom kandidatnom kluci",
                "Funkcna zavislost": "Hodnoty atributu relacie urcuje "
                                     "jednoznacne hodnotu ineho atributu tej istej relacie ",
                "Tranzitivna funkcna zavislost": "Y je funkcne zavisli na X ak viem Y jednoznacne urcit podla X",
                "ACID": "Atomicita, Konzistencia, Izolacia, Trvalost",
                "Tranzakcia": "Skupina prikazov ktora sa musi vykonat spolu alebo nevykonat vobec",
                "Stavy tranzakcie": "Active, particularly confirmed, confirmed, fail, aborted",
                "Zurnal": "mechanizmus sluzi na zaznamenavanie jednotlivych databazovych operacii",
                "Redo, undo": "Potvrd, Vrat",
                "Graf precedencie tranzakcii": "Orientovany graf"
                                               "\nkazdy jeho vrchol reprezentuje 1 tranzakciu"
                                               "\nkazda hrana reprezentuje dvojicu konfliktnych operacii",
                "Zamky": "Sluzia aby si tranzakcia rezervovala isty databazovy objek pocas "
                         "doby nevyhnutnej na vykonanie operacie",
                "2PL": "2 fazy"
                       "\nnajskor zamyka"
                       "\npotom odomyka"
                       "\ninak nekonzistentna analyza"
                       "\nnezabrani deadlocku",
                "Matica kompatibility": "read-read povolene inak zakazane",
                "kategorie chybnych stavov": "1. chyby tranzakcie"
                                             "\n2. zrutenie systemu"
                                             "\n3. poskodenie disku so stratou dat",
                "obecne integritne obmedzenia": "1. Entitne integritne obmedzenie"
                                                "\n\t- Zaistuje uplnost a unikatnost PK"
                                                "\n\t- Zamedzi ulozeniu dat ktore by boli v tychto stlpcoch rovnake"
                                                "\n2. Domenove integritne obmedzenie"
                                                "\n\t- Zaistuje dodrziavanie datovych typov/domen "
                                                "definovanych u stlpcov databazovej tabulky"
                                                "\n3. Referencne integritne obmedzenia"
                                                "\n\t- zaoberaju sa vztahom 2 tabuliek, "
                                                "kde ich relacia je urcena vazbou PK a FK"
                                                "\n\t- hodnota FK v jednej tabulke musi odpovedat hodnote KK v "
                                                "inej tabulke, alebo musi byt prazdna"
                }
    list_ipp = {
        "Syntax": "- Syntax jazyka definuje strukturu program, t.j. to akym sposobom je dovolene jednotlive "
                  "konstrukcie radit za seba\n- pre definiciu syntaxe pre ucely popisu jazyka pre programatorov "
                  "sa v sucastnosti pouziva budto syntakticke grafy, BNF ci EBNF, alebo gramatiky",
        "Semantika": "popis/definicia jednotlivych syntaktickych konstrukcii, sposob ich vyhodnotenia, "
                     "spracovania atd.",
        "Formalizmy semantiky": "Axiomaticka, Operacna, Denotacna semantika",
        "Axiomaticka semantika": "Pre kazdu syntakticku konstrukciu definuje mnozinu axiomov ktore musia byt "
                                 "splnene aby bola dana konstrukcia platna",
        "Operacna semantika": "Definuje semantiku spravania programu ako postupnost prechodov medzi jednotlivymi "
                              "stavmi",
        "Denotacna semantika": "program je definovany ako matematicka funkcia ktora zobrazuje vstupy na vystupy",
        "Deklaracia": "Uplne vymedzuje atributy danej entity. Moze byt explicitna aj implicitna",
        "Definicia": "Uplne vymedzuje atributy danej entity a dalej u premennych definuje sposob alokacie pamate a u "
                     "funkcii/procedur dalej telo funkcie",
        "Vlastnosti premennych": "Meno"
                                 "\nAdresa a umiestnenie"
                                 "\nHodnoty ktore moze nadobudat"
                                 "\ntyp"
                                 "\ndoba zivota"
                                 "\nrozsah platnosti",
        "Vazby": "Mnozina typov ktore moze premenna nadobudat, priradenie typu premennej, mnozina hodnot ktore moze"
                 "premenna nadobudat, hodnota ktoru premenna nadobuda, mnozina vyznamov operatora, konkretny vyznam "
                 "operatora, interna reprezentacia literalu",
        "Rozsah platnosti premennej": "Urcuje tu cast program kedy je mozne s premennou pracovat",
        "Doba zivota premennej": "Je casovy interval pocas ktoreho je pre danu premennu alokovana pamat",
        "Nestrukturovane jazyky": "Su vacsinou netypovane",
        "Formalna baza": "Je taky formalny prostriedok, ktory umoznuje exaktne popisat vsetky konstrukcie daneho "
                         "jazyka"
                         "\n\t- sluzi k tomu aby bolo mozne iste vlastnosti jazyka formalne dokazat ci overit"
                         "\n\t- casto sa jedna o semantiku, bezospornost jazyka atd."
                         "\n\t- ak je formalna baza k dispozicii dopredu, tak sa jedna o najidealnejsie voditko pre"
                         "implementaciu"
                         "\n\t- nestrukturovane jazyky formalnu bazu nemaju",
        "Otvoreny podprogram": "Ulozeny v ramci hlavneho tela programu, nema definovane pevne rozhranie, vstup sa deje"
                               "skokom na prikaz ktory ma vypocet programu zacat",
        "Strukturovane jazyky": "Su typicky typovane",
        "Floyd-Hoare logika": "Formalne overenie vlastnosti algoritmov"
                              "\n- pre kazdy programovy prvok je definovana podmienka splnenia pred a po vykonanej "
                              "operacie popisanej danym prvkom",
        "Objektovo orientovane programovanie": "Je sposob abstrakcie, kedy algoritmus implementujeme ako mnozinu "
                                               "zapuzdrujucich, vzajomne komunikujucich entit, kde kazda z nich ma "
                                               "plnu vypocetnu mocnost celeho pocitaca",
        "Objektovo orientovany system": "Sklada sa z jedneho alebo viacerych objektov, ktore spolu komunikuju a "
                                        "interaguju pri spolupraci na riesenie daneho problemu",
        "Objekt": "Je entita zapuzdrujuca stavove informacie a poskytujuca sadu operacii nad tymto objektom"
                  "alebo jeho castami",
        "Sprava": "Komunikacna jednotka medzi dvoma lubovolnymi objektami"
                  "\nOkrem svojho mena moze obsahovat aj dodatocne informacie v podobe parametrov",
        "Metody": "Implementuju vsetko spravanie objektov",
        "Koncept objektu": "Spojuju data a funkcionalitu do spolocnych jednotiek zvanych objekty, z ktorych sa potom"
                           "sklada vysledny OOP, su zakladnymi jednotkami modularity a struktury v OOP",
        "Koncept abstrakcie": "Schopnost programu zjednodusovat/ignorovat/zapuzdrovat niektore aspekty informacii "
                              "ci vlastnosti objektov, s ktorymi program pracuje",
        "Koncept zapuzdrenia": "Zaistuje uz na urovni definicie semantiky jazyka, ze uzivatel nemoze menit interny stav"
                               " objektov lubovolnym sposobom ale musi k tomu vyuzivat poskytovane rozhrania",
        "Koncept polymorfizmus (mnohotvarnost)": "Vyuziva mechanizmus zasielania sprav"
                                                 "\nnamiesto bezneho volania podprogramov v strukturovanom "
                                                 "programovani sa v OOJ vyuziva mechanizmus zasielania sprav",
        "Koncept dedicnost": "Sposob ako implementovat zdielane spravanie"
                             "\nNove objekty tak mozu zdielat a rozsirovat spravanie tych existujucich bez nutnosti "
                             "vsetko znovu reimplementovat",
        "Identita": "Porovnava ci sa jedna o ten isty objekt",
        "Zhodnost": "Porovnava objekty na zaklade obsahov",
        "Trieda": "Sablona podla ktorej mozu byt vytvarane objekty"
                  "\nstara sa o spravu protokolu objektu",
        "Rusenie objektov v pamati": "Automaticky, Manualne",
        "Jednoducha dedicnost": "Kazdy potomok ma max 1 priameho predka",
        "Viacnasobna dedicnost": "Kazdy potomok moze dedit od viacerych priamych predkov",
        "Dedicnost implementacie": "Okrem atributov su dedene aj cele metody vratane ich implementacii",
        "Dedicnost rozhrania": "V praxi sa jedna o predpis alebo zoznam metod, ktore je nutne v potomkovi "
                               "implementovat",
        "Vyzadovana dedicnost": "Ak je instancia triedy alebo z nej zdedenej triedy vyzadovana na mieste parametru "
                                "metody",
        "Staticky typovany jazyk": "Urcuje mnozinu operacii ktore objekt podporuje uz v dobe prekladu",
        "Dynamicky typovany jazyk": "Kontrolu operacii ktore objekt podporuje robi az pocas behu programu",
        "Redefinicia metod": "Moznost jazyka definovat pre metodu podtriedy novu, specifickejsiu implementaciu "
                             "ako je v jej nadtriede",
        "Prototypovo orientovane jazyky": "Tieto jazyky unifikuju svoj navrh tym, ze poznaju iba jediny typ objektu "
                                          "a nevyclenuju samostatne objekty reprezentujuce triedy",
        "UML": "Jednotny graficky jazyk pre jednotnu specifikaciu, vizualizaciu, konstrukciu a dokumentaciu pri "
               "objektovo orientovanej analyze a navrhu",
        "Menny priestor": "Je z programatorskeho hladiska kontajner pre identifikatory, vnutri kontajneru nie su dva"
                          "rovnake identifikatory",
        "Modifikator viditelnosti": "Mechanizmus pritomny v mnohych dnesnych OOJ, ktory ma za ulohu menit moznost "
                                    "pristupu k roznym entitam jazyka",
        "Pretazovanie metod": "Je vlastnost umoznujuca definovat v triede viac metod s rovnakym menom, musia sa "
                              "odlisovat v typoch alebo pocte premennych",
        "Staticka vs triedna metoda": "Triedna sa viaze na triedu (obsahuje parameter self)"
                                      "\nStaticka metoda - pristup iba k statickym polozkam",
        "Vyhody objektovej orientacie": "Analogia medzi softwarovym modelom a realnym modelom"
                                        "\nFlexibilita takychto softwarovych modelov"
                                        "\nIch znovupouzitelnost",
        "Vyhody a nevyhody OOP": "Toto tu nejdem pisat",
        "Metoda": "Odpovedajuca zapuzdrujuca funkcia objektu",
        "Protokol (rozhranie)": "Mnozina vsetkych sprav, ktorym objekt rozumie",
        "Instancia": "Proces samotneho vytvarania objektu",
        "Konstruktor": "Naplnuje alebo inicializuje datove polozky",
        "Kopie objektov": "Hlboka kopia, plytka kopia",
        "Ucely dedicnosti": "Znovu pouzitie definovanej triedy"
                            "\nZaistenie spatnej kompatibility"
                            "\nK indikacii, ze nove spravanie specializuje ine uz exist. spravanie"
                            "\nPre zdielanie kodu",
        "S-kalkul volnost": "Rozsah platnosti premennej",
        "UML pohlad": "Projekcia systemu na jedno ci viac diagramov UML",
        "UML diagram": "Struktura podobna obecnemu grafu obsahujuca mnozinu grafickych prvkov prepojenych vztahmi",
        "Zakladne stavebne bloky UML": "Prvky - Strukturne, Spravania, Zoskupovania, Doplnkove"
                                       "\nVztahy - Asociacia, Zavislost, Agregacia-Kompozicia, Generalizacia, "
                                       "Realizacia",
        "UML Trieda": "Rozdelena na 3 bloky: Nazov, zoznam atributov, zoznam operacii",
        "UML Atributy": "Prvky objektu, u nich mozno definovat typ, meno, implicitnu hodnotu a viditelnost",
        "UML Operacia": "Vo vacsine pripadov odpoveda metodam triedy"
                        "\n- pomenovane spravanie triedy",
        "Diagram tried": "Graf symbolov tried, rozhrani, zoskupeni a dalsich strukturnych prvkov prepojenych "
                         "statickymi vztahmi",
        "UML Realizacia": "Vztah medzi rozhranim a implementacnou triedou",
        "UML Generalizacia": "Staticky vztah medzi obecnejsiou a specifickejsiou entitou",
        "UML Agregacia": "Vyjadruje zlozenie entity zo skupiny komponentnych entit",
        "UML Kompozicia": "Specialny pripad agregacie"
                          "\nKazda komponenta moze patrit iba 1 celku",
        "UML Zavislost": "Vztah medzi prvkami, ked zmena 1 elementu ma vplyv na zavysli element",
        "UML Ortogonalita": "Nezavislost technologie na kontexte",
        "Klasifikacia jazykov podla urcovania typov pri zapise": "Beztypove, Netypovane, Typovane",
        "Klasifikacia jazykov podla doby vytvorenia vazby premennej na typ": "Staticky, dynamicky typovane",
        "Klasifikacia jazykov podla sposobu typovej kontroly": "Staticka, dynamicka",
        "Klasifikacia jazykov podla dokladnosti typovej kontroly": "Silne typovane, slabo typovane",
        "Rozhranie": "Schema, ktore deklaruje zoznam metod",
        "Implementacie sablon": "staticky"
                                "\ndynamicky"
                                "\nad hoc",
        "Sablona": "Mechanizmus, ktory umoznuje parametrizaciu definicii datovych typov",
        "Virtualny stroj": "Specialna softwarova vrstva, kde jej primarnym ucelom je oddelit pre beziacu aplikaciu "
                           "hardwarove specifikacie pocitaca, na ktorom je vykonavana",
        "Bytekod": "Medzikod",
        "Navrhove vzory": "Obecne znovupouzitelne riesenia casto sa vyskytujucich problemov v programovom navrhu"
                          "\nSystematicky nazyva, vysvetluje a vyhodnocuje dolezity a v OOS sa opakujuci navrh",
        "Jedinacik": "Navrhovy vzor"
                     "\nObmedzuje moznosti vytvarat z triedy viac ako 1 instanciu",
        "Co vieme odvodit z typu premennej": "Velkost ktoru zabera v pamati"
                                             "\nObor hodnot, ktore moze nadobudat"
                                             "\nMnozinu operacii, ktore nad nou mozeme vykonavat",
        "Model vypoctu": "Imperativne jazyky, deklarativne jazyky",
        "Riesenie cyklickej zavislosti": "Spojenim zavyslich modulov do jedneho",
        "Strict evaluation": "Parametry su vyhodnocovane pred volanim funkcie a ich hodnota je prekopirovana",
        "Modularne jazyky": "Dalsi vyvojovy stupen programovacich jazykov"
                            "\nViac podporuje timovu pracu a to tym sposobom ze je mozne program poskladat z "
                            "podprogramov, ktore na sebe nemusia byt zavysle",
        "Dynamicke semanticke chyby pri jazyku C": "Delenie nulou"
                                                   "\nPohyb v poli mimo index po uzivatelskom vstupe"
                                                   "\nZla praca s pamatou"
                                                   "\nOverflow/Underflow",
        "SLD rezolucia": "Pouziva sa v jazyku prolog"
                         "\nVstupny text spracovava na zaklade jednoducheho schematu:"
                         "\n\tklauzule su vyberane postupne zhora dolu"
                         "\n\tparadigma na riadku su vyberane zlava doprava postupne"
                         "\nV priebehu dochadza k unifikacii medzi premennymi a hodnotami, ktore sa objavuju na "
                         "prislusnych poziciach parametrov",
        "Co musi splnovat prekladac modularnych jazykov, aby mohol byt po prelozeni vsetkych modulov uspesne"
        "zostaveny vysledny program": "Musi generovat relativny kod, ktory nasledne ide do linkeru, ktory "
                                      "to prevedie na absolutny alebo relokatibilny kod. Musi generovat vsetky "
                                      "potrebne symboly, a vsetky exportovane, vyvazene symboly",
        "Tranzistentny a perzistentny objekt rozdiely": "Perzistentny:"
                                                        "\n\tObjekt je po znovuspusteni aplikacie/systemu k dispozicii "
                                                        "v rovnakom stave a s rovnakou identitou ako pred vypnutim "
                                                        "aplikacie/systemu"
                                                        "\nTranzistentny:"
                                                        "\n\tVznika za behu programu a zanika najneskor s jeho "
                                                        "ukoncenim",
        "Klasifikujte jazyk Python": "- Python je multiparadigmaticky programovaci jazyk"
                                     "\n- Dynamicky typovany"
                                     "\n- Sprava pamate pomocou garbage collectoru"
                                     "\n- Modularny - rozsiruje sa cez moduly"
    }
    list_izg = {
        "Co je potreba pre farbu?": "Svetlo (Nositel informacie)"
                                    "\nObjekt (Ma fyzicke vlastnosti)"
                                    "\nPozorovatel (Vnima farbu)",
        "Achromaticke a chromaticke svetlo": "Achromaticke (biele) - Rovnomerne zastupenie vlnovych dlzok"
                                             "\nChromaticke (farebne) - Nerovnomerne zastupenie vlnovych dlzok",
        "Charakteristika svetla": "Jas - Intenzita svetla"
                                  "\nSytost - Cistota farby svetla, sirka farebneho svetla"
                                  "\nSvetlost - Velkost achromatickej zlozky svetla farby"
                                  "\nOdtien - Dominantna vlnova dlzka svetla",
        "RGB": "Odpoveda aditivnemu miesaniu farieb"
               "\nPraca/miesanie so svetlom"
               "\nMonitory, projektory, kamery atd"
               "\nZakladne farby: Red, Green, Blue"
               "\nZlozenim zakladnych farieb maximalnej intenzity vznika biela farba",
        "CMY": "Odpoveda subtraktivnemu miesaniu farieb"
               "\nPraca/miesanie s pigmentom"
               "\nTlaciaren"
               "\nZakladne farby: Cyan, Magenta, Yellow"
               "\nZlozenim zakladnych farieb maximalnej intenzity vznika cierna farba",
        "HSV": "Uzivatelsky orientovany model"
               "\nNastavuje odtien, sytost a svetlost"
               "\nPri limitoch ubytku jasu klesa zaroven aj sytost",
        "Fragment shader": "Vykonava operacie nad jednotlivymi fragmentami sceny (vysledka, teda 2D obrazu), stara "
                           "sa napriklad o urcenie farieb pixelov ci zobrazenie textur vo vyslednom renderi",
        "Z-buffer (datova struktura, velkost, hodnoty obsahuje, kde sa s nim pracuje, pre aky typ 3D objektov je "
        "vhodny?)": "Struktura - 2D pole"
                    "\nVelkost - framebuffer-velkost rozlisenia color bufferu"
                    "\nHodnoty obsahuje - Obsahuje Z suradnice najblizsich bodov ploch"
                    "\nPracuje sa v GPU"
                    "\nVhodny pre 3D objekty - Netransparentne objekty, polygony, trojuholniky",
        "Riadkove vyplnanie": "Pouziva sa pre vyplnanie mnohouholnikov"
                              "\nV skratke prechadza oblasti po riadkoch a useky"
                              " ktore lezia vnutri objektu su vyfarbene"
                              "\nMusime brat do uvahy parny a neparny pocet "
                              "priesecnikov riadkov a modelu + obrazok",
        "Pseudokod pre vykreslenie krivky ktora je zadana parametrickym vyjadrenim "
        "G(t) = [x(t), y(t)]": "for(float t = 0; t <= 1; t += 0.01) {"
                               "\n\tdrawPoint(x(t), y(t));"
                               "\n}",
        "B-rep 4 charakteristiky": "Objekt je popisany pomocou svojho povrchu - hranice"
                                   "\nInformacie o vnutornej strukture objektu neni ulozena"
                                   "\nObjekt definovany pomocou: vrcholov, hran, sten",
        "Graficky kontext (popis a co obsahuje)": "Datova struktura, ktora drzi specificke informacie potrebne pre "
                                                  "vykreslenie na rozne vystupne zariadenia"
                                                  "\nObsahuje:"
                                                  "\n\tparametry vystupneho zariadenia"
                                                  "\n\tsirka a vyska kresliacej plochy"
                                                  "\n\ttransformacia vystupu",
        "Supersampling": "Kazdy pixel obrazu je rozdeleny na niekolko vzoriek, subpixely, z ktorych je konvolucnym "
                         "filtrom zlozena vysledna hodnota pixelu"
                         "\n- vyhladzuje vysledny obraz, hrany a textury"
                         "\n- vyrazny pokles vykonu zobrazeni",
        "Co je mozne nanasat na 3D texturu": "1. Odraz svetla"
                                             "\n2. Zmena normaloveho vektora"
                                             "\n3. Drsnost"
                                             "\n4. Priehladnost",
        "Texturou nanasane informacie 3D objekty": "Farba povrchu"
                                                   "\nPriehladnost"
                                                   "\nModifikacia normaly"
                                                   "\nModifikacia geometrie"
                                                   "\nOsvetlenie",
        "Ambient, diffuse, specular zlozka v phongovi": "Ambient - svetelny sum, rozptylene svetelne pozadie"
                                                        "\nDiffuse - Odraz svetla do vsetkych smerov, umoznuje nam "
                                                        "vidiet objekty, zavysi na normale a polohe svetla"
                                                        "\nSpecular - prasatka, zalezi na polohe pozorovatela a polohe "
                                                        "svetla",
        "Prevod obrazu na ciernobiely": "1. Prevedieme na odtien sedi"
                                        "\n- Prahovanie"
                                        "\n- Nahodne prahovanie"
                                        "\n- Distribucia chyby"
                                        "\n- Maticove rozptylenie",
        "3 metody nanasania struktur": "Inverzne mapovacie funkcie"
                                       "\nPremietanie textur"
                                       "\nMapovanie 3D textur"
                                       "\nUV mapovanie",
        "2 situacie kde sa mozeme stretnut s aliasingom": "Na sikmych ciarach, v texturach",
        "Barycentricek rovnice": "l1 + l2 + l3 = 1 -> bod nalezi trojuholniku"
                                 "\nl1 + l2 + l3 != 1 -> bod lezi mimo trojuholnika"
                                 "\nl1 = 0; l2 + l3 = 1 -> bod lezi na hrane protilahlej p1",
        "Smernicovy tvar rovnice priamky a popisat": "y = kx + q"
                                                     "\ny - funkcna hodnota, vysledok funkcie"
                                                     "\nx - argument funkcie"
                                                     "\nq - offset po osi Y"
                                                     "\nk - smernica",
        "Rovnica pre vypocet suradnice xp priesecnika usecky s hranicou orezavacieho okna"
        "": "(x2 - x1) / (y2 - y1) = (xp - x1) / (yp - y1)",
        "Rovnica krivky a kde sa vyuziva": "Parametricke vyjadrenie krivky:"
                                           "\n\tx(t) = ax*t^3 + bx*t^2 + cx*t + dx"
                                           "\n\ty(t) = ay*t^3 + by*t^2 + cy*t + dy"
                                           "\nVyuzitie:"
                                           "\n\tDefinicia objektu"
                                           "\n\tDefinicia fronty"
                                           "\n\tKreativna grafika"
                                           "\n\turcovanie drahy objektu pri animacii"
                                           "\n\tSablonovanie",
        "Rozdiel medzi fragment, vertex shaderom": "Vertex - poskytnut finalnu transformaciu dalej do grafickej "
                                                   "pipeline"
                                                   "\nFragment - poskytnut farbu/texturovanie kazdemu pixelu",
        "Transformacna matica posunu v smere (x, y, z)": "1 0 0 0"
                                                         "\n0 1 0 0"
                                                         "\n0 0 1 0"
                                                         "\nx y z 1",
        "Matica inverzneho posunutia": "1  0  0"
                                       "\n0  1  0"
                                       "\n-x -y 1",
        "Zmena meritka matica (scale) (x, y)": "x 0 0"
                                               "\n0 y 0"
                                               "\n0 0 1",
        "Matica inverzny scale": "1/x 0   0"
                                 "\n0   1/y 0"
                                 "\n0   0   1",
        "Matica otocenia": "cos(a)  sin(a) 0"
                           "\n-sin(a) cos(a) 0"
                           "\n0       0      1",
        "Matica skosenia (shear)": "1   shy 0"
                                   "\nshx 1   0"
                                   "\n0   0   1",
        "Matica inverzne skosenie (shear)": "1    -shy 0"
                                            "\n-shx 1    0"
                                            "\n0    0    1",
        "Inverzne riadkove vyplnovanie": "Vyhladavanie priesecniku sa robi inverziou od priesecnika az po okraj obrazu"
                                         "\nnepotrebuje zoradovat priesecniky",
        "Multisampling": "Rovnako ako pri supersamplingu su pixely rozdelene na viac subpixelov, ktore lezia na "
                         "okrajoch polygonu, su pocitane zvlast. Hustejsie vzorkovanie pri hranach objektu, mimo "
                         "objek a vnutri objektu redsie vzorkovanie vyrazne vyhladzuje hrany objektov, samotnej "
                         "textury menej",
        "Phongovo tienovanie": "Pri rasterizacii prebieha interpolacia normal z vrcholu"
                               "\nOsvetlovaci model sa pocita pre kazdy pixel"
                               "\nJe potreba poznat priemerne normaly vo vrcholoch"
                               "\nZohladnuje sa zakrivenie povrchov objektov"
                               "\nVelmi kvalitne vysledky, realisticke zobrazenie"
                               "\nNarocna implementacia",
        "Popiste zakladni bloky zobrazovaciho retezce (OpenGL)": "viz papier",
        "Pinedov algoritmus": "Pracuje iba s konvexnymi utvarmi, najcastejsie s trojuholnikmi"
                              "\nSpociva v rozdeleni oblasti na polroviny hran"
                              "\nPre kazdy pixel strany trojuholnika vypocitame hranovu funkciu. Ak je hranova "
                              "funkcia >= 0, bod je vnutri objektu. Bod vnutri objektu sa znaci pomocou +",
        "MipMap": "Zmensena verzia textury, ktora sa pouziva pri texturovani vzdialenych polygonov",
        "Vertex shader": "Obsahuje program ktory transformuje"
                         "\nVstupy: Build-in attribute variables"
                         "\nVystupy: Special output variables",
        "Texturovanie pomocou suradnic": "U vacsiny \"Beznych\" objektov neni mozne najst jedinu analyticku funkciu "
                                         "popisujucu povrch. Preto musime provadet mapovanie po castiach. Spojitost "
                                         "casti zaisti \"Texturovacie suradnice\". Tie pre kazdy povrchovy vrchol "
                                         "objektu definuju odpovedajuce suradnice textury. Hodnoty texturovacich "
                                         "suradnic medzi definovanymi hodnotami vo vrcholoch su linearne interpolovane",
        "Algoritmus de casteljau": "Rekurzivny algoritmus vykreslovania bezbarierovych kriviek"
                                   "\nPlynie z rekurentnej definicie pre bernsteinove polynomy"
                                   "\nUseky riadiaceho polynomu su delene v pomere hodnot t a 1 - t",
        "Ray-tracing a radiozita": "viz papier",
        "CSG pre 3D modely": "Objekt je popisany stromom z: 3D primitiv, transformacii, bool operacii"
                             "\nMoznost vzniku singularit"
                             "\nPo kazdej novej operacii prebieha regeneracia stromu"
                             "\nMoznost parametrizacie operacii v strome",
        "3 riesenia tienovani": "1. Flat shading"
                                "\n2. Gouraud shading"
                                "\n3. Phong shading",
        "Flat shading": "- Vyhodnocuje sa stredovy pixel polygonu"
                        "\n- Konstantna farba"
                        "\n- Nezohladnuje sa zakrivenie"
                        "\n- Gradient tienu je plynuly, ale lahka implementacia aj v HW",
        "Gouraud shading": "- Vyhodnocuju sa pixely vo vrcholoch"
                           "\n- Interpolacia farieb pri rasterizacii"
                           "\n- Zohladnuje sa zakryvenie"
                           "\n- Potreba poznat priemerne normaly vo vrcholoch"
                           "\n- Gradient plynuly, ale nie uplne presny, lahka implementacia aj v HW",
        "Phong shading": "- Interpolacia normal z vrcholov"
                         "\n- Vyhodnocuje sa kazdy pixel"
                         "\n- Zohladnuje sa zakryvenie"
                         "\n- Potreba poznat priemerne normaly vo vrcholoch"
                         "\n- Gradient plynuly, vysoko presny, narocna implementacia",
        "Is = Il * rs ( V * R ) ^ ns popisat": "rs - koeficient reflexie"
                                               "\nns - koeficient ostrosti"
                                               "\nIs - vysledna intenzita svetla"
                                               "\nIl - intenzita prichadzajuceho svetla"
                                               "\nR - vektor odrazu"
                                               "\nV - vektor k pozorovatelovi",
        "Id = Il * rd * C ( n * L ) popisat": "rd - koeficient difuzneho odrazu"
                                              "\nC - farba povrchu"
                                              "\nL - vektor dopadajuceho paprsku"
                                              "\nn - normalovy vektor plochy"
                                              "\nIl - intenzita dopadajuceho paprsku"
                                              "\nId - vysledna intenzia"
    }

    file = None
    # Loading arguments
    if len(sys.argv) != 2:
        # Wrong program input arguments
        print("Error in starting file")
        print()
        print_help_message()
        exit(-1)
    else:
        file = sys.argv[1]
        if not os.path.exists(file):
            print("Error: File passed as an argument doesn't exists")
            exit(-1)

    subject = Subject(file)

    clear()
    run = True
    while run:
        choice = None
        try:
            choice = input("Select choice: ").lower()
        except KeyboardInterrupt:
            run = False
            continue

        if choice == 'r':
            clear()
            subject.print_ran_choice()
        elif choice == 'a':
            subject.print_answer()
        elif choice == 'c' or choice == 'count':
            clear()
            subject.print_count()
        elif choice == 'all':
            subject.print_all()
        elif choice == 'quit':
            run = False
        elif choice == 'h' or choice == 'help':
            print_help_message()
        else:
            print("I don't understand the choice, see help for known choices")
