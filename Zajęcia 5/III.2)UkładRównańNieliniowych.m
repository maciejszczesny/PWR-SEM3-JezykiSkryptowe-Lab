function F = uklad(a)
  x = a(1)
  y = a(2)
  
  F(1)=x^2 + 2*x*y^2 - 40;
  F(2)=2*x^2 - 3*y^2 + 19;
end

wynik = fsolve(@uklad,[1,1])
#[1,1] to punkt startowy dla fsolve dla 2 zmiennych, wektor w kierunku kt�rego ma szuka� rozwi�za�???
#Ten uk�ad ma 2 rozwi�zania rzeczywiste, [2,3] i [2,-3], szukaj�c w kier ujemnych y znajdziemy drugie rozwi�zanie.
