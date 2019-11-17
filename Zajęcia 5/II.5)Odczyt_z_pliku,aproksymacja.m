dane = csvread('dane.csv'); #dane = odczyt z pliku .csv
t = dane(2:end,1); #t = w kolumnie pierwszej, od drugiego wiersza do koñca
R = dane(2:end,2); #R = w kolumnie drugiej, od drugiego wiersza do koñca
p = polyfit(t,R,1); #zwraca wspó³czynniki wielomianu o stopniu n czyli 1, który da siê wpasowaæ w dane
y = polyval(p,t); #zwraca wartoœæ wielomianu p (wyliczonego wczeœniej) w punkcie(punktach) t
plot(t, R, 'ro;Rezystancja;', t, y, 'b-;aproksymacja;') #rysowanie 2 rzeczy na 1 wspólnym wykresie
xlabel('Czas [s]'); #ustawienie labela osii X
ylabel('Rezystancja [Ohm]'); #ustawienie labela osii Y
grid on; #w³¹czenie podgl¹du siatki na wykresie