import datetime
import csv



### kod a dokładniej funkcje przynależności względem czasu premiery są zależne od aktualnego roku kalendarzowego  
def currentYear():
        today = datetime.date.today()
        year = today.timetuple()
        return year.tm_year  


### FUNCKJE PRZYNALEŻNOŚCI ### =======================================================

### Filmy w miarę nowe ### ===========================================================  
def relativelyNew(y_movie_list,y_current):  
        ralativelyNewList = []
        for year in y_movie_list:
            if int(year) > y_current-1:
                ralativelyNewList.append(0)
                
            elif int(year) < y_current-8:
                ralativelyNewList.append(0)
                
            elif (int(year) >= y_current-5) and (int(year)<=y_current-4):
                ralativelyNewList.append(1)
                
            elif (int(year) >=y_current-8) and (int(year)<y_current-5):
                x = (int(year)-(y_current-8))/3
                ralativelyNewList.append(x)
                
            else:
                x = ((y_current-1)-int(year))/3
                ralativelyNewList.append(x)
        #print()        
        #print(ralativelyNewList)
        return ralativelyNewList


### Filmy Średnio stare ### ============================================================
def MediumOld(y_movie_list,y_current):
        mediumOldList = []
        for year in y_movie_list:
            if int(year) > y_current-14:
                mediumOldList.append(0)
                
            elif int(year) < y_current-30:
                mediumOldList.append(0)
                
            elif (int(year) >= y_current-24) and (int(year)<=y_current-20):
                mediumOldList.append(1)
                
            elif (int(year) >=y_current-30) and (int(year)<y_current-24):
                x = (int(year)-(y_current-30))/6
                mediumOldList.append(x)
                
            else:
                x = ((y_current-14)-int(year))/6
                mediumOldList.append(x)
        #print()        
        #print(mediumOldList)
        return mediumOldList


### Filmy stare ### ============================================================      
def Old(y_movie_list,y_current):
        oldList = []
        for year in y_movie_list:
            if int(year) > y_current-30:
                oldList.append(0)
                
            elif int(year) <= y_current-44:
                oldList.append(1)
                
            else:
                x = ((y_current-30) - int(year))/14
                oldList.append(x)
        #print()        
        #print(oldList)
        return oldList

### Filmy niedługie ### ============================================================
def notLongTime(time_list):
        notLongList = []
        for time in time_list:
            if int(time) > 100:
                notLongList.append(0)
                
            elif int(time) < 60:
                notLongList.append(0)
                
            elif (int(time) >= 78) and (int(time)<= 82):
                notLongList.append(1)
                
            elif (int(time) >= 60) and (int(time)< 78):
                x = (int(time)-60)/18
                notLongList.append(x)
                
            else:
                x = (100-int(time))/18
                notLongList.append(x)
        #print()        
        #print(notLongList)
        return notLongList

### Filmy średnio długie ### ============================================================--  
def mediumLongTime(time_list):
        mediumLongList = []
        for time in time_list:
            if int(time) > 119:
                mediumLongList.append(0)
                
            elif int(time) < 99:
                mediumLongList.append(0)
                
            elif (int(time) >= 108) and (int(time)<= 110):
                mediumLongList.append(1)
                
            elif (int(time) >= 99) and (int(time)< 107):
                x = (int(time)-99)/9
                mediumLongList.append(x)
                
            else:
                x = (119-int(time))/9
                mediumLongList.append(x)
        #print()        
        #print(mediumLongList)
        return mediumLongList
        
### Filmy dość długie ### ============================================================
def quiteLongTime(time_list):
        quiteLongList = []
        for time in time_list:
            if int(time) > 142:
                quiteLongList.append(0)
                
            elif int(time) < 110:
                quiteLongList.append(0)
                
            elif (int(time) == 126):
                quiteLongList.append(1)
                
            elif (int(time) >= 110) and (int(time)< 126):
                x = (int(time)-110)/16
                quiteLongList.append(x)
                
            else:
                x = (142-int(time))/16
                quiteLongList.append(x)
        #print()        
        #print(quiteLongList)   
        return quiteLongList


### TWORZENIE PODZBIORÓW FILMÓW WDG WZORU podanego w zadaniu ### ==================================================

# Funckja zwracająca t-normę minimum
def minimum(listTime,listYear):
        if (listYear==0) and (listTime == 0):
            return 0
            
        elif listYear == 0:
            return 0
            
        elif listTime == 0:
            return 0
            
        elif listYear > listTime:
            return listTime
            
        else:
            return listYear

# Zbiór filmu odpowiadającego t-normie minimum filmów starych i dość długich
def old_and_quiteLong(listTime,listYear,csv_base):
        filmListIndex = []
        x = len(listTime)
        newlist =[]
        for nr in range(x):
            film = minimum(listTime[nr] , listYear[nr])
            newlist.append(film)
        
        for i in range(x):
            if max(newlist) != 0:                       # TUTAJ ZACHODZI ,,SORTOWANIE LISTY'' - DZIĘKI CZEMU NASZE WYNIKI W PLIKU CSV BĘDĄ OD NAJBARDZIEJ PASUJĄCYHC DO NAJMNIEJ 
                index = (newlist.index(max(newlist)))   #MAX() - zawsze szukamy największej wartości - najabrdziej pasujących do podzbioru
                filmListIndex.append(index+1)  # szukamy indeksu na którym jest największa wartość a następnie zapisujemy ten indeks w nowej liście ( +1 dlatego że potem uzyjemy tych indeksów do zapisania danych na podstawie pierwotnej bazy wiedzy a tam na indeksie 0 są nagłówki kolumn)
                newlist[index]= 0 # następnie w tej liscie zamieniamy tą największą wartość na 0 bo już jej indeks został zapisany i idziemy do kolejnego więc nie chcemy aby nadal pozostała w tabeli ta przed chwilą przetwarzana - ,,największa wartość"
                
           
        
        with open('Stare_i_dosc_dlugie.csv','w',encoding='utf8',newline="") as f:          
            WRITE = csv.writer(f)
            WRITE.writerow(csv_base[0]) #zapisujemy nagłówki kolumn
            for i in filmListIndex:
                WRITE.writerow(csv_base[i]) # zapisujemy te wiersze które odpowiadają filmom o wcześniej wybranych i posortowanych indeksach

# Zbiór filmów odpowiadającego k-nonormie maksimum filmów średnio starych LUB niedługich
def mediumOldY_or_notLong(listYear,listTime,csv_base):
        filmListIndex = []
        x = len(listTime)
        newlist =[]
        for nr in range(x):
            film = max(listTime[nr] , listYear[nr]) #k-norma maksimum
            newlist.append(film)
        
        for i in range(x):
            if max(newlist) != 0:
                index = (newlist.index(max(newlist)))
                filmListIndex.append(index+1)
                newlist[index]= 0
           
       
        with open('srednioStare_lub_nieDlugie.csv','w',encoding='utf8',newline="") as f:
            WRITE = csv.writer(f)
            WRITE.writerow(csv_base[0])
            for i in filmListIndex:
                WRITE.writerow(csv_base[i])

# Zbiór filmów odpowiadającego t-normie minimum filmów w miarę nowych i średnio długich
def rNewY_and_mediumLong(listYear,listTime,csv_base):
        filmListIndex = []
        x = len(listTime)
        newlist =[]
        for nr in range(x):
            film = minimum(listTime[nr] , listYear[nr])
            newlist.append(film)
        
        for i in range(x):
            if max(newlist) != 0:
                index = (newlist.index(max(newlist)))
                filmListIndex.append(index+1)
                newlist[index]= 0
           
       
        with open('filmy_w_miare_nowe_i_srednio_dlugie.csv','w',encoding='utf8',newline="") as f:           
            WRITE = csv.writer(f)
            WRITE.writerow(csv_base[0])
            for i in filmListIndex:
                WRITE.writerow(csv_base[i])


def main():
        #database = input("Wprowadź nazwę bazy danych: ")
        list_year = []
        list_time = []
        csv_base = []
        
        for line in csv.reader(open("database.csv")): #database
            csv_base.append(line)
            
        for line in csv.DictReader(open("database.csv"),delimiter=";"): #database

            list_time.append(line['Czas'])
            list_year.append(line['Rok produkcji'])

        ### Lata
        rNewY = relativelyNew(list_year,currentYear())
        mediumOldY = MediumOld(list_year,currentYear())
        oldY = Old(list_year,currentYear())
        
        ## Minuty
        notLong = notLongTime(list_time)
        mediumLong = mediumLongTime(list_time)
        quiteLong = quiteLongTime(list_time)
        
        ## utworzenie nowych plików z konkretnymi cechami
        old_and_quiteLong(quiteLong,oldY,csv_base)
        mediumOldY_or_notLong(mediumOldY,notLong,csv_base)
        rNewY_and_mediumLong(rNewY,mediumLong,csv_base)
        print("Pliki utworzono.")
        input("Kliknij 'enter' by zakończyć działanie programu")
        
main()