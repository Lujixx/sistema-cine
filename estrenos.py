import tkinter as tk
from PIL import Image, ImageTk
import subprocess


def retrocederaMenu(estrenos):
    estrenos.withdraw()
    subprocess.Popen(["python", "menu.py"])

ventana = tk.Tk()
ventana.geometry("500x1000") 
ventana.configure(bg="black")
ventana.title("Próximos Estrenos")


botonRetroceder = tk.Button(ventana, text="Atras", command=lambda: retrocederaMenu(ventana))
botonRetroceder.place(x=450, y=670)



peliculas = [
    {"titulo": "Película 1", "descripcion": "Coraline Jones (a la que presta su voz Dakota Fanning) es una niña de 11 años llena de vida, de curiosidad y mucho más aventurera de lo que haría suponer su edad. Acaba de trasladarse con sus padres (Teri Hatcher, John Hodgman) de Michigan a Oregón. Echa de menos a sus amigos, y al ver que sus padres están desbordados por el trabajo, decide encontrar alguna distracción en el vecindario. Wybie Lovat (Robert Bailey Jr), un chico de su edad que vive en el barrio, quiere ser su amigo, pero ella le considera un pesado. Visita a sus vecinas, dos excéntricas actrices inglesas llamadas Srta. Spink y Srta. Forcible (Jennifer Saunders y Dawn French) y al aún más excéntrico ruso Sr. Bobinsky (Ian McShane). Después de estas experiencias, Coraline empieza a dudar seriamente de si su nuevo hogar le ofrecerá alguna diversión...", "imagen": "coraline.jpg"},
    {"titulo": "Película 2", "descripcion": "Una joven escritora norteamericana, Edith Cushing, se enamora de un apuesto inglés, Thomas Sharp, que ha llegado a la ciudad en busca de financiación para futuros negocios. Cuando el padre de la joven muere en extrañas circunstancias, Thomas convence a Edith para que le acompañe a su lujosa mansión familiar, Allerdalle Hall, una enorme propiedad de estilo gótico escondida en los montes de Inglaterra y plagada de misterios y peligros.", "imagen": "cumbre.jpg"},
    {"titulo": "Película 3", "descripcion": "Tras las inesperada muerte de su querido perro Sparky, el joven Victor aprovecha el poder de la ciencia para devolver a su mejor amigo a la vida - con algunos ajustes menores. Intenta esconder las costuras caseras de su creación pero cuando Sparky salga, los compañeros de Victor, sus profesores y la ciudad entera aprenderán que conseguir una nueva correa que lo agarre a la vida puede ser monstruoso.", "imagen": "frank.jpg"},
    {"titulo": "Película 4", "descripcion": "Al inicio del filme se nos presenta a Halloween Town y su celebridad más famosa, Jack Skellington (Jack Skeleton en la versión española), el Rey Calabaza. Vemos cómo, a pesar de que Jack es amado y respetado por los habitantes de la ciudad, sufre de depresión, ya que se encuentra cansado de celebrar, año tras año, la fiesta de Halloween. En medio de su desdicha, sale a caminar sin rumbo por un cementerio junto a Zero, su perro fantasma. Más tarde, descubre un círculo de árboles que nunca antes había visto. Cada árbol tiene una puerta representativa de la festividad a la que pertenece la ciudad a la que conduce. Jack se siente inmediatamente atraído por el que tiene la forma de un árbol lleno de adornos. Cuando Jack abre la puerta del Árbol de la Navidad, es transportado a un pueblo lleno de nieve, luces y felicidad. Jack queda abrumado con todos los colores y alegría que llenan el ambiente, y cae en la cuenta de que es lo que estaba buscando.", "imagen": "jack.jpg"},
    {"titulo": "Película 5", "descripcion": "Adam (Alec Baldwin) y Bárbara (Geena Davis) mueren en un accidente de coche poco tiempo después de estrenar su nueva casa. Los nuevos propietarios son los Deetz: Charles Deetz (Jeffrey Jones), su mujer Delia Deetz (Catherine O'Hara), que interpreta a una extravagante escultora, y la hija de Charles, Lydia Deetz (Winona Ryder), en el papel de una sombría muchacha que detesta a su padre y a su madrastra. Lo que los Deetz no imaginan es que Adam y Bárbara, convertidos ya en fantasmas, están molestos con su llegada y, por accidente y sin desearlo verdaderamente, le piden ayuda a Beetlejuice (Michael Keaton), un desagradable, gritón y chapucero bioexorcista que utilizará sus poco recomendables métodos para echar a los vivos (los Deetz) de la casa.", "imagen": "juice.jpg"},
    {"titulo": "Película 6", "descripcion": "Durante una noche de Navidad, una anciana le cuenta a su nieta la historia de Eduardo Manostijeras (Johnny Depp), un muchacho creado por un extravagante inventor (Vincent Price) que no pudo acabar su obra, dejando al joven con cuchillas en lugar de dedos.", "imagen": "tijera.jpg"}
]

imagenes_tk = [ImageTk.PhotoImage(Image.open(pelicula["imagen"]).resize((100, 150))) for pelicula in peliculas]

for i, pelicula in enumerate(peliculas):
    boton = tk.Button(
        ventana,
        text=pelicula["titulo"],
        font=("Bryant Light", 14),
        bg="#08546C",
        fg="white",
        image=imagenes_tk[i]
    )
    boton.grid(row=i, column=0, padx=10, pady=10)

    descripcion = tk.Text(
        ventana,
        wrap=tk.WORD,  
        width=40,  
        height=6,  
        font=("verdana", 10),
        bg="#E4E4E4"
    )
    descripcion.insert("1.0", pelicula["descripcion"]) 
    descripcion.config(state=tk.DISABLED) 
    descripcion.grid(row=i, column=1, padx=10, pady=10)

ventana.mainloop()
