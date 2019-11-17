dane = csvread('dane.csv'); #dane = odczyt z pliku .csv
t = dane(2:end,1); #t = w kolumnie pierwszej, od drugiego wiersza do ko�ca
R = dane(2:end,2); #R = w kolumnie drugiej, od drugiego wiersza do ko�ca
p = polyfit(t,R,1); #zwraca wsp�czynniki wielomianu o stopniu n czyli 1, kt�ry da si� wpasowa� w dane
y = polyval(p,t); #zwraca warto�� wielomianu p (wyliczonego wcze�niej) w punkcie(punktach) t
plot(t, R, 'ro;Rezystancja;', t, y, 'b-;aproksymacja;') #rysowanie 2 rzeczy na 1 wsp�lnym wykresie
xlabel('Czas [s]'); #ustawienie labela osii X
ylabel('Rezystancja [Ohm]'); #ustawienie labela osii Y
grid on; #w��czenie podgl�du siatki na wykresie