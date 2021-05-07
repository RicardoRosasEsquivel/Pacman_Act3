#Ricardo Rosas ESquivel
#A00829089

#Refelexión
#Aprendí la dinámica y uso de vectores para mejorar el rensdimineto de un programa, considero que antes de poder 
#experiemtar con los comandos de clasifiaciones de vecotres facilita y enriquece las tareas , permite codigos más
#ocomplejos y representar situaciónes rreales en simulaciónes a computadora. Considero que eta actividad reforzó
#mi conocimeinto en phyton ademas de dotarme con las herramientas necesarias para avanzar en mis proyectos.
#El mayor problema a enfrentar fue el mapa, la manera más facil de editarlo fue crear una columna entera donde
#estuviera despejado el mapa y empezar a meter obstáculos con las formas que deseara, acabando con las iniciales TEC como obstáculo
#Mi segundo reto a abordar fue el desplegar el nombre, debido a que intené usar el mismo turtle write para desplegar
#actualizando el score y mi nombre, pero opté al fonal por manejar dos entes separados evitandome la sobre escritura.
#El tercer problema se presentó al camiar los colores de los fantasmas y sus velocidades, el última parte fue fácil 
#adempas añadí diferentres velocidades en su movimento buscando un cambio de dinamismo al juego, pero me resultó dificil asimilar
#como se manejaban las velocidades y posiciónes de los fantasmas, al estar aacostumbrado a programar con MATLAB
#por la naturalesa de mi carrera, el no tener los valores de mis variables y entidades a la vista es un poco desconcertante 
#____Fecha: 6-Mayo-2021

from random import choice
from turtle import *
from random import randrange
from freegames import floor, vector

state = {'score': 0}              #Almacena el score
path = Turtle(visible=False)      #Hace invisible la flecha y crea una turtle
writer = Turtle(visible=False)    #Hace invisible la flecha y crea 1 turtle ,score
writer1 = Turtle(visible=False)    #Hace invisible la flecha y crea 1 turtle, Nombre
#Con esto creamos 2 turtles
aim = vector(5, 0)                #Dirección de pacman
pacman = vector(-40, -80)         #Crea un pacman vectorial en la dirección -40, -80

ghosts = [                        #Crea a los fantasmas vectoriales como Posición - Dirección
    [vector(-180, 160), vector(5, 0)],    #1Fantasma se mueve 5 steps a la derecha
    [vector(-180, -160), vector(0, 5)],   #2Fantasma se mueve 5 steps hacia arriba
    [vector(100, 160), vector(0, -5)],    #3Fantasma se mueve 5 steps hacia abajo
    [vector(100, -160), vector(-5, 0)],   #4Fantasma se mueve 5 steps a la izquierda
]

tiles = [                          #Crea el mapa del juego
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Esquina inferior izquierda dibuja un square
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)
    if tiles[index] == 0:             #Si la calda del mapa es 0 da flaso
        return False

    index = offset(point + 19)
    if tiles[index] == 0:             #Si la calda del mapa es 0 da flaso
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    "Draw world using path."
    bgcolor('black')          #Color de los bloques de obstáculors
    path.color('blue')        #Color del camino libre
    #Recorre la lista de tiles
    for index in range(len(tiles)):
        #Extrae el valor que existe en la posición idex
        tile = tiles[index]
        
        #Si tile es 1
        if tile > 0:                  #Calcula de posición(X,Y) donde se dibuja el cuadro 
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(3, 'white')

def move():
    #__________________Despliega el nombre el autos
    def info_alumnos():

        writer1.up()
        writer1.goto(0,190)
        writer1.color('orange')
        writer1.write('Ricardo Rosas E.', align='left', font=('Arial', 8, 'normal'))
        
        
    #Lista de colores para los fantasmas
    colores = ['red', 'green', 'orange', 'grey']
    
    "Move pacman and all ghosts."
    writer.undo()                    #Despliega el contador de puntos
    #writer.write(state['score'])
    valor = state['score']
    writer.write(f'Score:{valor}')
    
    info_alumnos()
    clear()                           #Liempia la ventana
    
    if valid(pacman + aim):           #Si es valido el movimiento, mueve a Pacman
        pacman.move(aim)

    index = offset(pacman)            #Retorna la posición de pecaman en el tablero 

    if tiles[index] == 1:             #Si la zona en la que estas ya está como 1
        tiles[index] = 2              #A esa posición se le da 2, osea ya comió una galleta
        state['score'] += 1
        #Calcula la posición de Pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)                  #Dibuja el square sin galleta

    up()
    goto(pacman.x + 10, pacman.y + 10)#Se va la posición del pacman
    dot(20, 'yellow')                 #Se dibuja a pacman por primera vez
    k = 0                             #Inicio la variavl de nuefor de fantasma
    #[vector(-180, 160), vector(5, 0)]
    for point, course in ghosts:
        #d2 = 50
        d1 = pacman - point
        if valid(point + course): #and d2 < d1 :      #Valida si el fantasma se puede mover en dirección course osea gost[posición, dirección]
            point.move(course)
        else:                          #Si no se puede mover poruqe no es valido
            options = [                #Opciones derecha, izquierda, arriba, abajo
                vector(0, 7),
                vector(6, 0),
                vector(-7, 0),
                vector(0, -6),
            ]
        
            #if d2 < 0:
            #    plan = options[randgange(0,2)]
            #else:
            #    plan = options[randrange(2,4)]
            plan = options[randrange(0,4)]  
            course.x = plan.x           #Mi nueva dirección para moverse
            course.y = plan.y
            #d2 = pacman - poin
            
        up()                            #Levanta el lapiz
        goto(point.x + 10, point.y + 10)# Mueve al fantasma 
        dot(15, colores[k])             #Dibuja el fantasma
        #dot(15, 'red')
        k = k+1

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            writer.goto(-130,0)       #Despliega "GAME OVER"
            writer.write('GAME OVER', font=('Arial', 30, 'normal'))
            return

    ontimer(move, 50)                #Vuelve a llamar la función dentro de 100 milisegundos


def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(450, 410, 370, 0)      #Se 
hideturtle()                 #Se esconde las turtle 
tracer(False)
#_________________Despliega la puntuación
#Posición del turtlo write osea el score
writer.goto(160, 160)
writer.color('white')
valor  = state['score']
writer.write(f'Score:{valor}')#Write despliega el score

listen()                      #Aciva la escucha de inputs
#Al detectar un input, se aplica la funsion change aplicada a
#la dirección de pacman en "aim"
onkey(lambda: change(5, 0), 'Right')  #Se usan lamdas porque no tiene argumentos 
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
#Llama la función world - dibuja eltablero 
world()
#Inicia la función de moviemiento
move()
#Inicia el loop gráfico, siempre dee ser el último en un programa Turtle
done()
