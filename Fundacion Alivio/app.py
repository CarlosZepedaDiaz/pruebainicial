from flask import Flask, render_template

app = Flask(__name__)

# Datos del equipo de profesionales, divididos en categorías
team = {
    "administrativos": [
        {
            "name": "Vanessa Lamilla Sasmay",
            "position": "Fundadora y Presidenta",
            "profession": "Ing. en Prevención de Riesgos",
            "photo": "img/vanessa_lamilla.jpg"
        },
        {
            "name": "Raisa Malinarich",
            "position": "Vicepresidenta",
            "profession": "Lic. Trabajo Social",
            "photo": "img/raisa_malinarich.jpg"
        },
        {
            "name": "Daniela Lamilla Sasmay",
            "position": "Tesorera",
            "profession": "",
            "photo": "img/daniela_lamilla.jpg"
        },
        {
            "name": "Karla Collao",
            "position": "Directora Área Social y Proyectos",
            "profession": "Trabajadora Social",
            "photo": "img/carla_collao.jpg"
        },
        {
            "name": "David Rojas",
            "position": " Área Jurídica",
            "profession": "Abogado",
            "photo": "img/david_rojas.jpg"
        },
        {
            "name": "Solangie Gómez Zapata",
            "position": "Área de Administración",
            "profession": "Administrativa",
            "photo": "img/solangie_gomez.jpg"
        },
        {
            "name": "Valeria Poblete García",
            "position": "Secretaria",
            "profession": "Administrativa",
            "photo": "img/valeria_poblete.jpg"
        },
    ],
    "salud": [
        {
            "name": "Susana Rojas Ángel",
            "position": "Encargada Área Infantil",
            "profession": "Mgtr. en Atención Integral para la Primera Infancia, Máster en Atención Temprana",
            "photo": "img/susana_rojas.jpg"
        },
        {
            "name": "Carla Villalobos",
            "position": "Área de Psicología",
            "profession": "Psicóloga",
            "photo": "img/carla_villalobos.jpg"
        },
        {
            "name": "Miguel Ángel Ramos",
            "position": "Líder en el Área de Salud",
            "profession": "Neuropsicólogo",
            "photo": "img/miguel_ramos.jpg"
        },
        {
            "name": "Javiera Álvarez Tapia",
            "position": "Área de Kinesiología",
            "profession": "Kinesióloga",
            "photo": "img/javiera_alvarez.jpg"
        },
        {
            "name": "Carlos Morales",
            "position": "Psicología Holística",
            "profession": "Lic. en Psicología",
            "photo": "img/carlos_morales.jpg"
        },

    ],
    "ingenieria": [
        {
            "name": "Allen Cáceres",
            "position": "Logística",
            "profession": "Prevencionista de Riesgos",
            "photo": "img/allen_caceres.jpg"
        },
        {
            "name": "Carlos Zepeda Díaz",
            "position": "Área TI",
            "profession": "Ing. en Computación",
            "photo": "img/carlos_zepeda.jpg"
        }

    ]
}

mission = "En la Fundación Alivio Chile nos dedicamos a ayudar a aliviar el dolor mediante el uso de medicina alternativa, la aplicación de tecnologías innovadoras como la realidad virtual, y el acompañamiento psicosocial. Ofrecemos asesoría social a personas con enfermedades que padecen dolor, brindando un apoyo integral y accesible. Nuestro compromiso es proporcionar alivio efectivo y sostenible, promoviendo la investigación, la educación y la sensibilización sobre el manejo del dolor en la comunidad. Trabajamos incansablemente para asegurar que cada individuo tenga la oportunidad de vivir una vida plena y libre de dolor, con dignidad y esperanza."

vision = "Ser la fundación líder en Chile en el alivio del dolor, estando presentes en cada lugar donde alguien necesite alivio, mediante la creación de centros especializados en el manejo del dolor a lo largo del país. Aspiramos a transformar vidas proporcionando acceso equitativo a tratamientos y cuidados compasivos, fomentando una cultura de empatía y apoyo en cada comunidad."

values = [
    ("Empatía", "Nos comprometemos a comprender y compartir el sentir de las personas, abordando tanto sus dolencias físicas como psicológicas con compasión y sensibilidad."),
    ("Integridad y Responsabilidad Social", "Actuamos con integridad y asumimos la responsabilidad social en nuestro trabajo con las comunidades actuales y futuras, garantizando un compromiso sólido y duradero."),
    ("Innovación y Tecnología", "Utilizamos la innovación y la tecnología para poner al alcance de quienes lo necesiten soluciones efectivas para el alivio del dolor, mejorando así su calidad de vida.")
]

novedades = [
    {"titulo": "Nuevo centro de atención", "descripcion": "Inauguramos un nuevo centro de atención en Santiago."},
    {"titulo": "Campaña de donación", "descripcion": "Únete a nuestra campaña de donación y ayuda a los más necesitados."}
]

@app.route('/')
def home():
    return render_template('index.html', novedades=novedades)

@app.route('/equipo')
def equipo():
    return render_template('equipo.html', team=team)

@app.route('/cause')
def cause():
    return render_template('cause.html', mission=mission, vision=vision, values=values)

@app.route('/how_to_help')
def how_to_help():
    return render_template('how_to_help.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/donaciones')
def donaciones():
    return render_template('donaciones.html')

@app.route('/voluntariado')
def voluntariado():
    return render_template('voluntariado.html')

@app.route('/donacion_bienes')
def donacion_bienes():
    return render_template('donacion_bienes.html')

@app.route('/promocion_redes')
def promocion_redes():
    return render_template('promocion_redes.html')

if __name__ == '__main__':
    app.run(debug=True)

