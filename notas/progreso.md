Hasta ahora tenemos la cuenta hecha sobre el modelo del libro de vibraciones

El modelo que usamos es el de vigas de Euler-Bernoulli.
Para plantear la ecuacion se analizan los esfuerzos de corte y las fuerzas que sostienen a la viga.
Viendo las unidades que resultaban nosotros nos dimos cuenta de un error de planteo en la ecuacion 6.91, en donde escribe como queda la ecuacion inhomogenea de movimiento.
Resulta que cuando fija la fuerza externa igual a cero, divide despues por $\rho A$ que seria la densidad lineal de la viga.
Esto hace que implicitamente cuando se resuelve la ecucacion inhomogenea haya que poner una fuerza por unidad de densidad lineal, ademas de por unidad de longitud que ya plantea el autor.


Con estas consideraciones la ecucacion que queda es separable en partes temporal y espacial.
Y por suerte hay un ejemplo resuelto de esta cuenta (pagina 560).


Las condiciones de contorno que nos parecieron mejores es pinned-pinned.
Pinned quiere decir el movimiento y el _bending moment_ es nulo pero no asi la derivada espacial y la fuerza de corte en el borde (ecuacion 6.95).
Con estas CC la ecuacion de movimiento queda basicamente igual a la de resonancia de una cuerda sin rozamiento, con una velocidad 
$$
    \omega _{0}= \sqrt{\frac{EI}{\rho A}} \left( \frac{n \pi}{l} \right) ^2  
$$ 
donde $E$ es el modulo de Young (79GPa para el oro), $I=\frac{\pi}{2} r^{4}$ es el segundo momento de inercia de un disco, $A=\pi r^2$ es el area del disco por lo que esos radios se cancelan, $n$ es el numero de modo y $l$ es la longitud del cable que se mueve.
De todos estos parametros el unico que no esta fijo es $l$, y ajustando $\omega$ para que el sistema resuene la frecuencia a la que vimos el pico en los datos de Juan ($f=930Hz$) obtenemos $l=13 mm$.

La expresion para la defleccion queda (usan $w$ para la defleccion y $\omega$ para la frecuencia)
$$
    w = \frac{f_{0}(t)}{\rho A} \sin \left(\frac{n \pi x}{l} \right) \frac{1}{\omega_{0}^2 - \omega^2}
$$ 


Nosotros queremos llegar a una fem de la forma
$$
    \epsilon = B_{0} \cos\left( \theta \right) \frac{dA}{dt}
$$ 
entonces si consideramos una fuerza $f_{0} = B_{0}I_{0}\cos(\omega t)$ nos queda la defleccion

$$
    w = \frac{ B_{0}I_{0}\cos(\omega t)}{\rho A} \sin \left(\frac{n \pi x}{l} \right) \frac{1}{\omega_{0}^2 - \omega^2}
$$ 
para saber el area de la espira multiplicamos $w$ por dos e integramos en x.
