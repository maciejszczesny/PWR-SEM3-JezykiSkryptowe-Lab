function F = uklad(a)
  x = a(1)
  y = a(2)
  
  F(1)=x^2 + 2*x*y^2 - 40;
  F(2)=2*x^2 - 3*y^2 + 19;
end

wynik = fsolve(@uklad,[1,1])
#[1,1] to punkt startowy dla fsolve dla 2 zmiennych, wektor w kierunku którego ma szukaæ rozwi¹zañ???
#Ten uk³ad ma 2 rozwi¹zania rzeczywiste, [2,3] i [2,-3], szukaj¹c w kier ujemnych y znajdziemy drugie rozwi¹zanie.
