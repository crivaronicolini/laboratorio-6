---
title: Informe de progreso 8/12
author: Ingrid Heuer & Marco Crivaro Nicolini
header-includes: |
    \usepackage[T1]{fontenc}
    \usepackage[bitstream-charter]{mathdesign}
    \usepackage{siunitx}
    \usepackage{physics}

linestretch: 1.2
margin: 1,5in
indent: true
---
Hasta ahora tenemos la cuenta hecha sobre el modelo del libro de vibraciones:

El modelo que usamos es el de vigas de Euler-Bernoulli.
Para plantear la ecuación se analizan los esfuerzos de corte y las fuerzas que sostienen a la viga.
Esto lo hace en la sección 6.5.
Viendo las unidades que resultaban nosotros nos dimos cuenta de un error de planteo en la ecuación 6.91, en donde escribe como queda la ecuación inhomogénea de movimiento.
$$
   \rho A \frac{\partial ^2 w(x,t)}{\partial t^2} + \frac{\partial ^2 }{\partial x^2} \left[ E I\frac{\partial ^2 w(x,t)}{\partial x^2}  \right] = f(x,t)
$$ 
donde $E$ es el modulo de Young (79GPa para el oro), $I=\frac{\pi}{2} r^{4}$ es el segundo momento de inercia de un disco, y $A=\pi r^2$ es el area de una sección de cable.
Resulta que cuando fija la fuerza externa igual a cero, divide después por $\rho A$ ($A=$ area de un corte del cable) que seria la densidad lineal de la viga.
Esto hace que implícitamente cuando se resuelve la ecuación in homogénea haya que poner una fuerza por unidad de densidad lineal, ademas de por unidad de longitud que ya plantea el autor.
$$
   \frac{\partial ^2 w(x,t)}{\partial t^2} + c^2 \frac{\partial ^4 w(x,t)}{\partial x^4} = \frac{f(x,t)}{\rho A}
$$ 
con $c^2 = \frac{EI}{\rho A}$.


Con estas consideraciones la ecuación que queda es separable en partes temporal y espacial.
Y por suerte hay un ejemplo resuelto de esta cuenta (pagina 560), que tiene una fuerza puntual en vez de uniforme.


La condición de contorno que nos pareció mejor es pinned-pinned.
Pinned quiere decir el movimiento y el _bending moment_ son nulos pero no así la derivada espacial y la fuerza de corte en el borde (ecuación 6.95).
Con estas CC la ecuación de movimiento queda básicamente igual a la de resonancia de una cuerda sin rozamiento, con una velocidad 
$$
    \omega _{0}= \sqrt{\frac{EI}{\rho A}} \left( \frac{n \pi}{l} \right) ^2  
$$ 
donde  $n$ es el numero de modo (quedan solo los impares) y $l$ es la longitud del cable que se mueve.
De todos estos parámetros el único que no esta fijo es $l$.
Ajustando $\omega$ para que el sistema resuene la frecuencia a la que vimos el pico en los datos de Juan ($f=930Hz$) obtenemos $l=13 mm$.

La expresión para la deflección queda (usan $w$ para la deflección y $\omega$ para la frecuencia)
$$
    w = \frac{f_{0}(t)}{\rho A} \sin \left(\frac{n \pi x}{l} \right) \frac{1}{\omega_{0}^2 - \omega^2}
$$ 


Nosotros queremos llegar a una fem de la forma
$$
    \epsilon = - B_{0} \cos\left( \theta \right) \frac{da}{dt}
$$ 
entonces si consideramos una fuerza $f_{0} = B_{0}I_{0}\cos(\omega t)$ nos queda la deflección
$$
    w = \frac{ B_{0}I_{0}\cos(\omega t)}{\rho A} \sin \left(\frac{n \pi x}{l} \right) \frac{1}{\omega_{0}^2 - \omega^2}
$$ 
para saber el area de la espira multiplicamos $w$ por dos e integramos en x de 0 a $l$ (el 2 se cancela con un 2 de la integral).
$$
    a = \frac{ B_{0}I_{0}\cos(\omega t)}{\rho A} \left( \frac{l}{n \pi} \right) \frac{1}{\omega_{0}^2 - \omega^2}
$$ 
ahora solo resta derivar la parte temporal y tenemos la fem resultante (el menos de derivar el coseno cancela el menos de la ley de Lenz)
$$
    \epsilon = \frac{l B ^2 _{0}I_{0} \cos(\theta)}{\rho A n \pi}  \frac{\omega}{\omega_{0}^2 - \omega^2} \sin(\omega t)
$$ 

Cosas importantes para notar

- El polo de resonancia depende cuárticamente con el largo del cable: un pequeño cambio en $l$ hace que la divergencia pueda ocurrir en otra region de frecuencias.
- Como el area es lineal con la corriente, la derivada temporal es la derivada temporal de la corriente, entonces todo lo que acompaña a $\frac{dI}{dt}$ lo podemos considerar como una impedancia $L$, y ya chequeamos que tenga unidades de Henrios.

Lo anterior es el estado del modelo hasta la semana anterior, antes de que nos pusiéramos a pensar en si esta fem esta en realidad en el circuito primario, y ese voltaje se suma al del generador.
Después de eso hicimos la cuenta de cuanto debería ser la fem para que la corriente cambie lo necesario para que veamos el ruido que vemos en el circuito secundario.
$$
    V_{primario} = \frac{R_{total}}{R_{muestra}} V_{secundario} = \frac{1060.1\Omega}{0.1\Omega} 50 \mu V = 530,05 mV
$$ 
Entonces para ver el ruido que vemos necesitamos que ademas del generador haya una fem sumada de $530mV$, que es mas grande que el generador.

Esto en la reunion anterior nos llevo a pensar que la fem debe estar contribuyendo una parte importante a la corriente que circula en el primario, y entonces lo anterior deja de ser tan valido.

Ahora estamos modelando el circuito como un RL, donde la L es lo que dijimos mas arriba, que depende de la frecuencia.
