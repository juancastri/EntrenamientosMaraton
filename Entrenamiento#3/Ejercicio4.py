#FINAL CHAMPIONS LEAGUE
""" En la final de Champions League se enfrentan el PSG y Bayer de Múnich, quien va 1-0 y el árbitro adiciona 6 minutos.
 Quedan escasas oportunidades de empatar para el grupo parisino. Neymar tiene el contragolpe a su mando;
  Mbappé se encuentra solo para recibir el pase de Neymar.
Ayuda a Mbappé a saber si puede llegar al pase que le enviará su compañero, sabiendo que parte desde un punto 
'i' hasta un punto 'f' de una matriz de orden N. Mientras que el equipo Bávaro ubica defensores en diferentes
 puntos de la cancha y están atentos al movimiento del francés.
Los defensas se representan con un ‘B’ en la matriz, los espacios donde se puede mover Mbappé se representan con un 
‘-’; pero Mbappé solo puede moverse en diagonal.

Input Format

La primera línea corresponde a un valor entero N que hace referencia al orden o dimensión cuadrada de la matriz. En las siguientes líneas se ingresarán los caracteres, indicando las posiciones de los jugadores en la cancha: 'B' son los jugadores del Bayer, I es la posición inicial donde está Mbappé, F es la posición final donde el francés debe de llegar, y los '-' (guiones) son los espacios de la cancha donde Mbappé puede desplazarse.

Constraints

3 ≤ N ≤ 9

Output Format

Ayuda al PSG a saber si pueden soñar con el alargue y luchar por llevarse la soñada orejona, de ser así realiza un programa que imprima “PSG”. En caso de que no puedan empatar el partido, se debe visualizar en pantalla “BAYER”.

Sample Input 0

5
- - - F -
- B - - B
- - - - B
I - - B -
- B - - -
Sample Output 0

PSG
Explanation 0

Mbappé tiene la posibilidad de marcar desplazándose en la diagonal derecha. En el camino no se encuentra con ningún oponente que esté sobre su eje. Por lo tanto se imprime PSG

Sample Input 1

5
- F B - -
B B - - B
- - I - -
- - - - -
- - - - -
Sample Output 1

BAYER
Explanation 1

Se imprime BAYER porque a la posición donde debe llegar Mbappé está cubierta por varios jugadores del Bayer y el francés no tiene manera alguna de llegar al balón porque el pase no fue preciso. """
