![enter image description here](https://raw.githubusercontent.com/Education-IT/Fuzzy-Sets/main/images/banner.png)
## Projekt zaliczeniowy na przedmiot - ***Sztuczna Inteligencja*** - **UAM**

> **Zrealizowano w czwartym semestrze studiów informatycznych.**

Zadanie polegało na wykorzystaniu **zbiorów rozmytych**, do napisania programu polecającego użytkownikowi filmy  
po wyznaczonych, rozmytych, **nieostrych filtrach**. Stworzyłem **6 funkcji**, przydzielających filmom wartość od **0** do **1**,  w zależności od zgodności z wyznaczonym filtrem.  Wynikiem działania programu są 3 nowo utworzone pliki `.csv` w których znajdują się polecane filmy, najbardziej pasujące do wyboru użytkownika.  Zawierają one dane które są posortowane pod względem wartości nadanej przez **funkcję stopnia przynależności**.

![enter image description here](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) ![enter image description here](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)[ ![enter image description here](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://education-it.pl/)
 ## 
**Program :**
 1)  Na starcie otrzymuje bazę danych filmów - `database.csv`.
 2) Przy pomocy zaimplementowanych 6 **funkcji matematycznych** - tworzy listy z wartościami stopnia przynależności. **( 0 - 1 )**
 3) Oblicza **t-normę minimum** oraz **k-normę maksimum** z 2. konkretnych wyznaczonych filtrów.
 4) Sortuje filmy od najbardziej do najmniej pasującego - biorąc pod uwagę tylko **dodatnie wartości** nadanych przez funkcję stopnia przynależności.
 4) Tworzy 3 pliki **.csv**: 
	a) `filmy_w_miare_nowe_i_srednio_dlugie.csv`
	b) `srednioStare_lub_nieDlugie.csv`
	c) `stare_i_dosc_dlugie.csv`


##  Funkcje:
> Przedstawione diagramy są poglądowe. Odzwierciedlają działanie funkcji tylko dla konkretnego zbioru filmów. (`database.csv`) 

> Funkcje, które określają dopasowanie do filtra z perspektywy daty powstania filmu - zostały stworzone przeze mnie tak, aby były uniwersalne i możliwe do wykorzystania również wielokrotnie w przyszłości - te funkcje przynależności biorą pod uwagę aktualnie trwający rok.

### 1. Filmy "w miarę nowe":


>$f(x)  =
  \begin{cases}
 x = [ rokFilmu - (aktualnyRok -8) ]/3 & \quad  \text{if } x > (aktualnyRok - 8) \text{ and } x < (aktualnyRok - 5)\\
  x=[ (aktualnyRok -1) - rokFilmu]/3 & \quad  \text{if } x > (aktulanyRok - 4) \text{ and }  x < (aktualnyRok - 1)\\
  1 & \quad  \text{if } x \ge (aktualnyRok - 5) \text{ and } x \le (aktualnyRok-4) \\
  0 & \quad  \text{if }  x \ge (aktualnyRok - 1) \text{ or } x < (aktualnyRok - 8)\\
  \end{cases}$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_w_miare_nowe.JPG?raw=true)

##
 ### 2. Filmy "średnio stare":

>$f(x)  =
  \begin{cases}
 x = [ rokFilmu - (aktualnyRok -30) ]/6 & \quad  \text{if } x > (aktualnyRok -30) \text{ and  } x < (aktualnyRok -20) \\
  x=[ (aktualnyRok - 14) - rokFilmu]/6 & \quad  \text{if } x > (aktualnyRok -20) \text{ and }  x < (aktualnyRok - 14)\\
  1 & \quad  \text{if } x \ge (aktulanyRok-24) \text{ and } x \le (aktualnyRok-20) \\
  0 & \quad  \text{if } x > (aktualnyRok - 14) \text{ or } x < (aktualnyRok - 30) \\
  \end{cases}$
  
  ![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/srednio_stary_film.JPG?raw=true)
##

 ### 3. Filmy "stare":

>$f(x)  =
  \begin{cases}
 x = [ rokFilmu - (aktualnyRok - 42) ]/12 & \quad  \text{if } x < (aktualnyRok - 30) \text{ and } x > (aktualnyRok-44)\\
  1 & \quad  \text{if } x \le (aktualnyRok -44)\\
 0 & \quad  \text{if }  x > (aktualnyRok - 30) \\
  \end{cases}$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_stare.JPG?raw=true)

##

### 4. Filmy "niedługie":

>$f(x)  =
  \begin{cases}
 x = [ czasFilmu - 60  ]/18 & \quad  \text{if } x\in (60 , 78])\\
  x=[100- czasFilmu]/18 & \quad  \text{if } x\in (82,100]\\
  1 & \quad  \text{if } x \in [78,82]\\
  0 & \quad  \text{dla pozostałych x-ów}\\
  \end{cases}$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_niedugie.JPG?raw=true)
##

### 5. Filmy "Średnio długie":

>$f(x)  =
  \begin{cases}
 x = [ czasFilmu - 99  ]/9 & \quad  \text{if } x\in (99 , 108])\\
  x=[119- czasFilmu]/9 & \quad  \text{if } x\in (110,119]\\
  1 & \quad  \text{if } x \in [108,110]\\
  0 & \quad  \text{dla pozostałych x-ów}\\
  \end{cases}$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_srednio_dlugie.JPG?raw=true)
##

### 6. Filmy "dość długie":

>$f(x)  =
  \begin{cases}
 x = [ czasFilmu - 110]/16 & \quad  \text{if } x\in (110, 126])\\
  x=[142- czasFilmu]/16 & \quad  \text{if } x\in (126,142]\\
  1 & \quad  \text{if } x = 126\\
  0 & \quad  \text{dla pozostałych x-ów}\\
  \end{cases}$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_dosc_dlugie.JPG?raw=true)
##


## Czego się nauczyłem
- Projekt ten był idealnym przećwiczeniem nowo zdobytej wiedzy z zakresu logiki rozmytej. 
- Uświadomił mi jak w rzeczywiście łatwy lecz przemyślany sposób można w praktyce skorzystać z logiki rozmytej do implementacji wielu programów użytkowych. Np.: sklepów E-comerce w których to najczęściej wyznaczamy ostry przedział cenowy który nas interesuje, chociaż delikatnie droższy produkt ale o konkretnych właściwościach może do nas bardziej przemawiać. Niestety sklepy tego typu przedstawiając nam wyniki wyszukiwania - nie biorą pod uwagę produktów które mogą delikatnie odstawać od pewnych parametrów ale zdecydowanie bardziej pasować w innych.