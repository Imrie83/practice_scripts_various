![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Slider 

Twoim zadaniem jest stworzenie prostego slidera. Realizacja podzielona jest na punkty. Pamiętaj, żeby trzymać się dokładnie ich treści i wykonywać je po kolei.

### Punkt 1
Zapoznaj się z kodem HTML i CSS dodanym do zadania. Do zrobienia slidera zazwyczaj używany odpowiednio ostylowanej listy, w której znajdują się obrazki.
Lista zazwyczaj spełnia następujące zależności:

1. Nie ma żadnych styli.
2. Ma szerokość i wysokość odpowiednią do wyświetlenia jednego obrazka.
3. Wszystkie obrazki mają tę samą szerokość i wysokość.
4. Wszystkie obrazki poza jednym są niewidoczne.

Dodaj w odpowiednie miejsce klasę ```slider``` w kodzie HTML.

### Punkt 2
Przygotuj do pracy plik **app.js**.
Następnie znajdź następujące elementy i zapisz je do zmiennych:

1. Guzik ```next```.
2. Guzik ```prev```.
3. Wszystkie elementy listy (zapisz do tablicy).

Dodaj też zmienną liczbową, która będzie określała indeks obrazka, który jest aktualnie widoczny (na początku będzie to pierwszy obrazek - czyli zmienna będzie wskazywała na indeks **0**).

Wypisz zmienne w konsoli, żeby upewnić się, czy zawierają poprawne dane.

### Punkt 3
Po dodaniu klasy ```slider``` zniknęły nam wszystkie obrazki. Dodaj do zerowego elementu naszej listy klasę ```visible```. Użyj odpowiednich zmiennych:
* tablicy z elementami listy,
* zmiennej, która określa widoczny element.
Po wejściu na stronę pierwszy obrazek powinien być widoczny.

### Punkt 4
Dodaj do guzików eventy reagujące na kliknięcie. Na początku mają tylko wypisywać w konsoli informacje o kliknięciu.

### Punkt 5
W evencie odpowiadającym za pokazanie następnego obrazka wykonaj następujące czynności:

1. Zabierz obecnie widocznemu obrazkowi klasę ```visible```.
2. Zwiększ zmienną trzymającą indeks obrazka, który jest aktualnie widoczny o jeden.
3. Dodaj obrazkowi, który powinien być widoczny, klasę ```visible```.
Użyj odpowiednich zmiennych (czyli tablicy z elementami listy oraz zmiennej, która określa, który element jest widoczny).

### Punkt 6
Wykonaj czynności w evencie dla guzika pokazującego poprzedni obrazek analogicznie do punktu 5.

### Punkt 7
Sprawdź, jak działa Twoja strona. Widzisz jakieś problemy związane ze sliderem? Napisz.

### Punkt 8
W poprzednim punkcie powinieneś zauważyć, że po wielokrotnym naciśnięciu guzika do przodu (albo do tyłu) obrazki znikają ze strony. Dzieje się tak dlatego, że zmienna określająca numer widocznego obrazka przyjmuje niepoprawną wartość (mniejszą od zera lub większą niż liczba elementów w naszej tablicy).
Jak temu zaradzić? W eventach dodaj **if-a**, który sprawdzi, czy wartość nie wyszła poza zakres. Jeżeli tak się stało, to program ma nastawić poprawną wartość:
* liczbą jest ujemna -> ostatni element,
* liczba równa się liczbie elementów lub jest większa -> **0**.



## Gallery

Napisz prostą galerię. Po naciśnięciu miniatury zdjęcia powinno się ono pokazywać w trybie pełnego ekranu.
Będzie się to działo przez dodanie nowego elementu w chwili, w której ktoś kliknie na daną miniaturę.
Zadanie podzielone jest na punkty. Pamiętaj, żeby trzymać się dokładnie treści punktów i robić je po kolei.

### Punkt 1
Zapoznaj się z kodem HTML i CSS dodanym do zadania. Do zrobienia galerii zazwyczaj używany odpowiednio wystylowanej listy, w której znajdują się obrazki.
Lista zazwyczaj spełnia następujące zależności:

1. Nie ma żadnych styli.
2. Ma szerokość i wysokość odpowiednią do wyświetlenia jednego obrazka.
3. Wszystkie obrazki mają tę samą szerokość i wysokość.
5. Wszystkie obrazki są widoczne.

W kodzie HTML dodaj (ręcznie) w odpowiednie miejsce klasę ```gallery```.

### Punkt 2
Przygotuj do pracy plik **app.js**.
Następnie znajdź następujące elementy i zapisz je do zmiennych:
1. Wszystkie elementy listy (zapisz do tablicy).
2. **Tag** ```body``` (będzie nam potrzebny do dodania elementu, który pokaże się na pełnym ekranie).

Wypisz zmienne w konsoli, żeby upewnić się, czy zawierają poprawne dane.

### Punkt 3
Do wszystkich obrazków dodaj event reagujący na kliknięcie. Najpierw może wypisywać "działa" w konsoli.

### Punkt 4
Zmodyfikuj event w taki sposób, żeby w konsoli wypisywał adres URL klikniętego obrazka. Użyj do tego ```this```.

### Punkt 5
Zauważ, że na górze pliku **app.js** jest zakomentowany kawałek kodu HTML. Jest to wzór elementu, który ma zostać dodany do strony.
Przeanalizuj go, a następnie zmodyfikuj event dla obrazków w taki sposób, żeby tworzyć takie elementy i dodawały go do **tagu** ```body```.
Pamiętaj o tym, żeby pod adres URL obrazka podłożyć odpowiednie dane.

### Punkt 6
Po kliknięciu na obrazek powinien nam się wyświetlać powiększony obrazek + guzik. Musisz teraz dopisać event reagujący na kliknięcie w guzik. Ma on spowodować usunięcie nowo stworzonego elementu z drzewa DOM.

### Punkt 7
Sprawdź, jak działa Twoja strona. Czy widzisz problemy? Napisz.



## Gallery with filter

Napisz galerię, w której będziesz chować obrazki z odpowiednimi tagami.
Po wpisaniu tagu w inpucie i kliknięciu guzika obrazki opisane tym tagiem powinny zniknąć/pojawić się.

Zadanie podzielone jest na punkty. Pamiętaj, żeby trzymać się dokładnie treści punktów i robić je po kolei.

### Punkt 1
Zapoznaj się z kodem HTML i CSS dodanym do zadania. Do zrobienia galerii zazwyczaj używamy diva o odpowiednim id.

### Punkt 2
Przygotuj do pracy plik **app.js**.
Następnie znajdź następujące elementy i zapisz je do zmiennych:

1. Wszystkie obrazki należące do galerii (zapisz do tablicy).
2. Guzik odpowiedzialny za znikanie obrazków.
3. Guzik odpowiedzialny za pojawianie się obrazków.
4. Input, do którego będziemy wprowadzać tagi.

Wypisz zmienne w konsoli, żeby upewnić się, czy zawierają poprawne dane.

### Punkt 3
Do guzików dopisz eventy na kliknięcie. Sprawdź, czy działają przez wyświetlenie w konsoli jakiegoś napisu.

### Punkt 4
Zmień eventy w taki sposób, żeby wyświetlały tekst wpisany w inpucie, a następnie czyściły go.
Zapisz ten tekst do zmiennej.

### Punkt 5
Zmień eventy w taki sposób, żeby dodatkowo wypisywały wszystkie tagi dla wszystkich obrazków (czyli musisz użyć pętli i datasetu).

### Punkt 6
Zmień eventy w taki sposób, żeby wyświetlały tylko i wyłącznie tagi, w których znajduje się napis z inputu (użyj do tego ```indexOf```).

### Punkt 7
Zmień eventy, w taki sposób, żeby zamiast wyświetlać tag dla obrazka (cały czas tylko dla tych, które mają odpowiedni tag), obrazek ten dostawał lub tracił (w zależności od guzika) klasę ```invisible```.

### Punkt 8
Sprawdź, jak działa Twoja strona. Czy widzisz problemy? Napisz.


## Menu

Napisz proste rozwijane menu. Zazwyczaj tworzy się je w liście (gdzie podmenu znajduje się w zagnieżdżonych listach).
Nasze menu ma dwa poziomy (następne poziomy możecie dorobić podobnie do pierwszego).

Zadanie podzielone jest na punkty. Pamiętaj, żeby trzymać się dokładnie treści punktów i robić je po kolei.

### Punkt 1
Zapoznaj się z kodem HTML i CSS dodanym do zadania. Menu będzie się dobrze wyświetlać, gdy dodasz odpowiednią **klasę** do odpowiedniego elementu.  

### Punkt 2
Przygotuj do pracy plik **app.js**.

Następnie znajdź elementy listy i zapisz je do zmiennych. Chodzi o wszystkie elementy listy głównej (te, które są widoczne), bez elementów listy zagnieżdżonych (te, które są niewidoczne). Pamiętaj o trzymaniu ich w tablicy.
Wypisz zmienne w konsoli, żeby upewnić się, czy zawierają poprawne dane.

### Punkt 3
Do każdego elementu listy (trzymanego w zmiennej) dodaj dwa eventy: ```mouseover``` i ```mouseout```. Wypisz coś w konsoli, żeby sprawdzić, czy eventy są dobrze podpięte.

### Punkt 4
Zmień eventy w taki sposób, żeby wyszukiwały pod listę elementu, na który najechaliśmy myszką (czyli zagnieżdżony  element **ul**).

### Punkt 5
Zmień eventy w taki sposób, żeby wiadomość z punktu 3. była wyświetlana, tylko gdy pod lista istnieje (czyli zwrócony element jest inny niż ```null```).

### Punkt 6
Zmień event ```mouseover```. Ma on nie wyświetlać informacji w konsoli, a powodować, że pod lista jest widoczna. Jeżeli nie wiesz, jak to zrobić, sprawdź kod CSS, żeby doczytać się, w jaki sposób lista staje się niewidoczna.

### Punkt 7
Zmień event ```mouseout```. Ma on nie wyświetlać informacji w konsoli, a powodować, że pod lista znowu znika.

### Punkt 8
Sprawdź, jak działa Twoja strona. Czy widzisz problemy? Napisz.



## Tooltips

Napisz tooltipy. Są to małe okienka wyskakujące po najechaniu na tekst z dodatkowymi informacjami. Jest to prosta wersja tego, co znajdziesz tutaj: https://jqueryui.com/tooltip/.

Tekst, który ma się wyświetlić w tooltipie, powinien być trzymany w datasecie.
Zadanie podzielone jest na punkty. Pamiętaj, żeby trzymać się dokładnie treści punktów i robić je po kolei.

### Punkt 1
Zapoznaj się z kodem HTML i CSS dodanym do zadania.  

### Punkt 2
Przygotuj do pracy plik **app.js**.
Następnie znajdź elementy o **klasie** ```tooltip``` (pamiętaj, że może być ich wiele) i zapisz je do zmiennych.
Wypisz zmienne w konsoli, żeby upewnić się, czy zawierają poprawne dane.

### Punkt 3
Do każdego elementu o **klasie** ```tooltip``` dodaj dwa eventy: ```mouseover``` i ```mouseout```. Dodaj do nich wyświetlanie jakiegoś napisu w konsoli, żeby sprawdzić, czy wszystko działa.

### Punkt 4
Zmodyfikuj eventy w taki sposób, żeby wyświetlały w konsoli tekst tooltipu, który będziemy dodawać.

### Punkt 5
Zmodyfikuj event ```mouseover```. Ma on dodawać nowy element do elementu, na którym jest wywoływany. Przykładowy element, który masz dodać, znajduje się w komentarzu na początku pliku **app.js**.

### Punkt 6
Zmodyfikuj event ```mouseout``` w taki sposób, żeby usuwał tooltip stworzony w poprzednim punkcie.

### Punkt 7
Sprawdź, jak działa Twoja strona. Czy widzisz problemy? Napisz.
