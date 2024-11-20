%Definimos el numero de Church segun el numero de elementos en una lista.
%El numero de Church de 0 es una lista vacia.
%Caso base
church(0, []).
%Sucesor de un numero de church. Devuelve false si el argumento no tiene la forma
%de un numero de Church.
church(N, [suc|N]) :- es_numero_church(N).

% Predicado para verificar si un elemento tiene la forma de un número de Church.
es_numero_church([]).
es_numero_church([suc|L]) :- es_numero_church(L).

%suma de dos numeros
suma(X,Y,Z) :- append(X,Y,Z).

%multiplicacion de dos numeros
multiplicacion([],_,[]). %Casos de multiplicacion por 0
multiplicacion(_,[],[]).
multiplicacion([suc|X],Y,Z) :- %Otros casos: agrega Y tantas veces como elementos tenga X
    multiplicacion(X,Y,Z1), %Z1 es el acumulador de cuantas veces se va sumando Y.
    suma(Y,Z1,Z).