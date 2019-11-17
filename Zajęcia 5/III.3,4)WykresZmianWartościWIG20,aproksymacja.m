dane = csvread('wig20.csv')

zamkniecie = dane(2:end,5);
zamkniecie = zamkniecie' #transpozycja �eby lenght dzia�a�o poprawnie
data = [1:1:length(zamkniecie)]; #zamiast odczytywa� daty tworz� tablic� od 1 do ilo�ci pomiar�w - do prezentacji wykresu
apro_1 = polyfit(data,zamkniecie,1); #wielomian pierwszego stopnia
aproksymacja_1 = polyval(apro_1,data); #wstawienie danych do wielomianu pierwszego stopnia
apro_2 = polyfit(data,zamkniecie,2); #wielomian drugiego stopnia
aproksymacja_2 = polyval(apro_2,data); #wstawienie danych do wielomianu drugiego stopnia

plot(data,zamkniecie,"b;Zmiany warto�ci WIG20;",data,aproksymacja_1,"r;Aproksymacja Liniowa;",data,aproksymacja_2,"g;Aproksymacja 2 stopnia;");
xlabel("Numer dnia");
ylabel("Warto��");
grid on;