import flet as ft
import flet_audio as fta
import random as ran

def main(page: ft.Page):
    async def playAudio():
        await dice_sound.play()
    async def diceChoice(e): 
        imageList = ["images1/numero1.png",
                     "images1/numero2.png",
                     "images1/numero3.png",
                     "images1/numero4.png",
                     "images1/numero5.png",
                     "images1/numero6.png"]
        chosenImage = ran.choice(imageList)
        randomImage.src = chosenImage
        if chosenImage == "images1/numero1.png":
            puntuacion.value = "Sacaste un 1"
        elif chosenImage == "images1/numero2.png":
            puntuacion.value = "Sacaste un 2"
        elif chosenImage == "images1/numero3.png":
            puntuacion.value = "Sacaste un 3"
        elif chosenImage == "images1/numero4.png":
            puntuacion.value = "Sacaste un 4"
        elif chosenImage == "images1/numero5.png":
            puntuacion.value = "Sacaste un 5"
        elif chosenImage == "images1/numero6.png":
            puntuacion.value = "Sacaste un 6"
        await playAudio()
        page.update()
    page.theme_mode= "LIGHT"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    
    dice_sound = fta.Audio(src="audio/audioDado.mp3", autoplay=False)
    randomImage = ft.Image(height=400, width=600, src="nada.png")
    changeImageButton = ft.Button(content="Prueba suerta suerte con el dado!", on_click=diceChoice)
    puntuacion = ft.Text(value="")
    page.add(puntuacion, randomImage, changeImageButton)
    pass

ft.run(main=main, assets_dir="DICE")