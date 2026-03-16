import flet as ft
import flet_audio as fta

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    cdp = 1
    score = 0

    preguntas = {0: {"image" : "images/logo.png",
                     "pregunta" : "Welcome to Penaltrivia!",},
             1: {"pregunta" : "¿Cual es el último ganador de la champions league?",
                 "image" : "images/championsTrophy.webp",
                 "opcion1" : "Manchester City",
                 "opcion2" : "Real Madrid",
                 "opcion3" : "PSG",
                 "opcion4" : "FC Barcelona",
                 "correcta" : "PSG",
                 "pista" : "El club es frances"},
             2: {"pregunta" : "¿Cual es la selección con mas mundiales?",
                 "image" : "images/copaMundial.png",
                 "opcion1" : "Brasil",
                 "opcion2" : "Colombia",
                 "opcion3" : "Paris",
                 "opcion4" : "España",
                 "correcta" : "Brasil",
                 "pista" : "Pele es de ese pais"},
             3: {"pregunta" : "¿Cual es la liga mas competitiva?",
                 "image" : "images/premier.png",
                 "opcion1" : "La Liga",
                 "opcion2" : "Liga DiMayor BetPlay",
                 "opcion3" : "Saudi League",
                 "opcion4" : "Premier League",
                 "correcta" : "Premier League",
                 "pista" : "Es de un país con monarquía"},
             4: {"pregunta" : "¿En que equipo está Mbappe?",
                 "image" : "images/clubesDeFutbol.png",
                 "opcion1" : "Atletico Madrid",
                 "opcion2" : "Real Madrid",
                 "opcion3" : "PSG",
                 "opcion4" : "FC Barcelona",
                 "correcta" : "Real Madrid",
                 "pista" : "Robos"},
             5: {"pregunta" : "¿Cual es el máximo goleador de la historia?",
                 "image" : "images/jugadores.png",
                 "opcion1" : "Cristiano Ronaldo",
                 "opcion2" : "Lionel Messi",
                 "opcion3" : "Lebron James",
                 "opcion4" : "Pélé",
                 "correcta" : "Cristiano Ronaldo",
                 "pista" : "No Coca Cola, si agua"},
             6: {"pregunta" : "¿Quien fue el ganador del Super Balón de Oro?",
                 "image" : "images/superBalonDeOro.png",
                 "opcion1" : "Puskas",
                 "opcion2" : "Alfredo di Stefano",
                 "opcion3" : "Roger Waters",
                 "opcion4" : "Freddie Mercury",
                 "correcta" : "Alfredo di Stefano",
                 "pista" : "Pasta"},
             7: {"pregunta" : "¿James Rodriguez de que país es?",
                 "image" : "images/james.png",
                 "opcion1" : "Venezuela",
                 "opcion2" : "Perú",
                 "opcion3" : "Colombia",
                 "opcion4" : "Panamá",
                 "correcta" : "Colombia",
                 "pista" : "Qbo"},
             8: {"pregunta" : "¿Que equipos juegan 'el clásico'? ",
                 "image" : "images/vs.png",
                 "opcion1" : "Los Dos de Manchester",
                 "opcion2" : "Atl. Nacional y Millonarios",
                 "opcion3" : "Atletico de Madrid y Real Madrid",
                 "opcion4" : "FC Barcelona y Real Madrid",
                 "correcta" : "FC Barcelona y Real Madrid",
                 "pista" : "negreira y lloros"},
             9: {"pregunta" : "¿En 2015 el Barca ganó la champions?",
                 "image" : "images/championsLeague.png",
                 "opcion1" : "Verdadero",
                 "opcion2" : "Falso",
                 "opcion3" : "Si y no",
                 "opcion4" : "Todas las anteriores",
                 "correcta" : "Verdadero",
                 "pista" : "El agua está mojada?"},
             10: {"pregunta" : "¿Quien es mejor jugador de la historia?",
                  "image" : "images/cabra.png",
                 "opcion1" : "Cristiano Ronaldo",
                 "opcion2" : "Alfonso",
                 "opcion3" : "Messi",
                 "opcion4" : "Maradona",
                 "correcta" : "Messi",
                 "pista" : "Ankara"},
             11: {"pregunta" : "Es turno de las preguntas de basketball",
                  "image" : "images/basketball.jpg"},
             12: {"pregunta" : "¿Cuántos puntos vale un tiro libre encestado?",
                  "image" : "images/tiroTres.jpg",
                 "opcion1" : "0 puntos",
                 "opcion2" : "1 punto",
                 "opcion3" : "2 puntos",
                 "opcion4" : "3 puntos",
                 "correcta" : "1 punto",
                 "pista" : "Piensa en la unidad mínima que puede alterar el marcador en una jugada individual."},
             13: {"pregunta" : "¿Cuántos jugadores de un mismo equipo pueden estar en la cancha al mismo tiempo?",
                  "image" : "images/equipoBasket.webp",
                 "opcion1" : "4 jugadores",
                 "opcion2" : "5 jugadores",
                 "opcion3" : "6 jugadores",
                 "opcion4" : "7 jugadores",
                 "correcta" : "5 jugadores",
                 "pista" : "Es el número necesario para cubrir las posiciones tradicionales desde el base hasta el pívot."},
             14: {"pregunta" : "¿Cómo se llama la acción de mover el balón rebotándolo contra el suelo con una mano?",
                  "image" : "images/dribbling.png",
                 "opcion1" : "Pasar",
                 "opcion2" : "Pivotar",
                 "opcion3" : "Driblar",
                 "opcion4" : "Lanzar",
                 "correcta" : "Driblar",
                 "pista" : "Es el lenguaje rítmico fundamental que permite avanzar legalmente por la pista."},
             15: {"pregunta" : "¿Qué parte del cuerpo no se puede usar para tocar el balón de forma intencionada?",
                  "image" : "images/player.webp",
                 "opcion1" : "La cabeza",
                 "opcion2" : "Los pies",
                 "opcion3" : "Los hombros",
                 "opcion4" : "Los codos",
                 "correcta" : "Los pies",
                 "pista" : "El reglamento penaliza cualquier contacto voluntario con las extremidades encargadas de la locomoción."},
             16: {"pregunta" : "¿Cuánto tiempo dura normalmente un partido de la NBA (tiempo de juego efectivo)?",
                 "image" : "images/partido.avif",
                 "opcion1" : "40 minutos",
                 "opcion2" : "48 minutos",
                 "opcion3" : "60 minutos",
                 "opcion4" : "24 minutos",
                 "correcta" : "48 minutos",
                 "pista" : "El tiempo total resulta de la suma de cuatro segmentos de igual duración reglamentaria."},
             17: {"pregunta" : "¿Qué ocurre si un jugador deja de botar el balón y luego vuelve a botarlo sin haberlo pasado o tirado?",
                  "image" : "images/screen.jpg",
                 "opcion1" : "Se llama 'dobles'",
                 "opcion2" : "Se llama 'pasos'",
                 "opcion3" : "Se llama 'falta'",
                 "opcion4" : "Es legal",
                 "correcta" : "Se llama 'dobles'",
                 "pista" : "Se incurre en una violación al intentar reiniciar una ventaja mecánica que ya había concluido."},
             18: {"pregunta" : "¿A qué altura se encuentra el aro de baloncesto profesional?",
                  "image" : "images/aro.jpg",
                 "opcion1" : "2.90 metros",
                 "opcion2" : "3.05 metros",
                 "opcion3" : "3.15 metros",
                 "opcion4" : "2.50 metros",
                 "correcta" : "3.05 metros",
                 "pista" : "Es una medida estandarizada basada en el sistema anglosajón que equivale a exactamente 10 pies."},
             19: {"pregunta" : "¿Cómo se llama el lanzamiento en el que el jugador salta e introduce el balón directamente en el aro con fuerza?",
                  "image" : "images/dunk.png",
                 "opcion1" : "Bandeja",
                 "opcion2" : "Gancho",
                 "opcion3" : "Donqueo",
                 "opcion4" : "Triple",
                 "correcta" : "Donqueo",
                 "pista" : "Es una maniobra de alta energía que busca asegurar la anotación desde una posición de máxima verticalidad."},
             20: {"pregunta" : "¿Cuál es el nombre de la línea que divide la zona de 2 puntos de la de 3 puntos?",
                  "image" : "images/linea.jpg",
                 "opcion1" : "Línea de banda",
                 "opcion2" : "Línea de fondo",
                 "opcion3" : "Línea de tres puntos",
                 "opcion4" : "Línea de medio campo",
                 "correcta" : "Línea de tres puntos",
                 "pista" : "Es el límite geométrico que define un cambio en el valor estratégico de la posesión."},
             21: {"pregunta" : "¿Qué jugador es famoso por inspirar la silueta del logo de la NBA?",
                  "image" : "images/jordan.jpg",
                 "opcion1" : "Michael Jordan",
                 "opcion2" : "Jerry West",
                 "opcion3" : "LeBron James",
                 "opcion4" : "Kobe Bryant",
                 "correcta" : "Jerry West",
                 "pista" : "Se le conoce como 'The Logo' debido a la icónica imagen capturada durante su etapa activa en la liga."},
             22: {"pregunta" : "Gracias por probar la trivia!",
                  "image" : "images/gracias.png"}}

    questionText = ft.Text(size=20)

    rg = ft.RadioGroup(
    content=ft.Column(
        controls=[
            ft.Radio(value="1", fill_color=ft.Colors.RED),
            ft.Radio(value="2", fill_color=ft.Colors.BLUE),
            ft.Radio(value="3", fill_color=ft.Colors.GREEN),
            ft.Radio(value="4", fill_color=ft.Colors.YELLOW),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
)

    resultText = ft.Text(size=40)

    transitionImage = ft.Image(src="images/DiscoTest.png", width=300)

    def playCorrectAudio():
        correct_sound.play()
    def mostrar_pista(e):
        pista_label.visible = True
        pista_label.value = preguntas[cdp].get("pista", "")
        page.update()
    def cargarpregunta():
        questionText.value = preguntas[cdp]["pregunta"]

        if cdp == 11:
            rg.visible = False
            transitionImage.src = preguntas[cdp]["image"]
            hintButton.visible = False
            pista_label.visible = False
        else:
            transitionImage.visible = True
            rg.visible = True
            hintButton.visible = True
            rg.content.controls[0].label = preguntas[cdp]["opcion1"]
            rg.content.controls[1].label = preguntas[cdp]["opcion2"]
            rg.content.controls[2].label = preguntas[cdp]["opcion3"]
            rg.content.controls[3].label = preguntas[cdp]["opcion4"]
            transitionImage.src = preguntas[cdp]["image"]

        rg.value = None
        page.update()

    def siguiente(e):
        nonlocal cdp, score
        if rg.value != None and "correcta" in preguntas[cdp]:

            if rg.value == "1":
                seleccion = preguntas[cdp]["opcion1"]
            if rg.value == "2":
                seleccion = preguntas[cdp]["opcion2"]
            if rg.value == "3":
                seleccion = preguntas[cdp]["opcion3"]
            if rg.value == "4":
                seleccion = preguntas[cdp]["opcion4"]

            if seleccion == preguntas[cdp]["correcta"]:
                score += 1
                playCorrectAudio()

        cdp += 1

        if cdp > 21:
            questionText.visible = False
            rg.visible = False
            nextButton.visible = False
            transitionImage.visible = False
            hintButton.visible = False
            pista_label.visible = False
            resultText.value = f"Puntuación Final: {score} / 20"
            restartButton.visible = True
        else:
            pista_label.visible = False
            cargarpregunta()

        page.update()
    def playBackSound():
        back_sound.play()
        page.update()
    def startquiz(e):
        startScreen.visible = False
        quizColumn.visible = True
        cargarpregunta()
        page.update()
        playBackSound()

    def restarquiz(e):
        nonlocal cdp, score
        cdp = 1
        score = 0
        resultText.value = ""
        questionText.visible = True
        rg.visible = True
        nextButton.visible = True
        restartButton.visible = False
        cargarpregunta()
        playBackSound()

    nextButton = ft.ElevatedButton("Siguiente Pregunta", on_click=siguiente)

    back_sound = fta.Audio(src="audio/LOFI MUSIC.wav", autoplay=True, volume=0.6)
    correct_sound = fta.Audio(src="audio/correct.mp3", autoplay=False)

    restartButton = ft.ElevatedButton("Reiniciar", on_click=restarquiz)
    restartButton.visible = False

    hintButton = ft.Button(
        icon=ft.Icons.QUESTION_MARK_OUTLINED,
        content="Pista",
        on_click=mostrar_pista, 
    )


    pista_label = ft.Text(size=20, color=ft.Colors.GREEN)

    startScreen = ft.Column(
        [
            ft.Text("Bienvenidos a Penaltrivia!", size=50),
            ft.Image(src="images/logo.png", width=300),
            ft.ElevatedButton("Empezar Quiz", on_click=startquiz)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    quizColumn = ft.Container(
    content=ft.Column(
        [
            hintButton,

            pista_label,
            
            questionText,

            transitionImage,

            rg,

            nextButton,

            resultText,

            restartButton,

        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True
    ),
    width=500,
    alignment=ft.Alignment(0, 0)
)

    quizColumn.visible = False

    page.add(startScreen, quizColumn)

ft.run(main=main, assets_dir="proyectoFinalArchivos")