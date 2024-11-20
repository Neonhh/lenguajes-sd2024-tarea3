%Definimos el tipo de datos
%persona(Nombre, Edad).

%Cantidad de personas en el conjunto
cantidad_personas([],0).
cantidad_personas([_|T],N) :- cantidad_personas(T,N1), N is N1+1.

%Subconjunto de personas mayores de edad
mayores_de_edad([],[]).
mayores_de_edad([persona(Nombre, Edad)|T], [persona(Nombre, Edad)|Mayores]) :-
    Edad >= 18, %Agrega la persona a la respuesta si es mayor de edad
    mayores_de_edad(T, Mayores).
mayores_de_edad([persona(_, Edad)|T], Mayores) :-
    Edad < 18, %No agrega la persona a la respuesta si es menor de edad
    mayores_de_edad(T, Mayores).
