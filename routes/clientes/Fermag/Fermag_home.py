from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Fermag_home = Blueprint("Fermag_home",__name__)

def getNavBar():
    return [
        ('Empresa','url_for','Fermag_home.FermagHome'),
        ('Noticias','url_for','Fermag_home.FermagNoticias'),
        ('Servicios','url_for','Fermag_home.FermagNoticias'),#,'Fermag_proyectos.FermagProyectos'),
        ('Proyectos','url_for','Fermag_home.FermagNoticias'),#,'Fermag_proyectos.FermagProyectos'),
        ('Ubicacion','link','https://www.google.com/maps/?hl=es'),
        ('Contacto','link','#footer')
    ]


@Fermag_home.route('/clientes/Fermag')
def FermagHome():
    NavBar = getNavBar()
    Servicios = [
        ('Domotica', 'https://www.zoomtecnologico.com/wp-content/uploads/2021/08/edificios-smart.jpg', '/noticias'),
        ('Energias renovables', 'https://www.cronista.com/files/image/143/143680/5ff79dbfe8b0e_600_315!.jpg?s=04accaac11dffedf92453f9dcee0e1e7&d=1665277260'),
        ('UPS', 'https://www.lage.com.mx/hubfs/Blog%20stock/preguntas-basicas-a-considerar-al-elegir-un-sistema-ups.jpg'),
        ('Instalaciones electricas', 'https://media.istockphoto.com/id/1338211923/es/foto/ingeniero-electricista-prueba-instalaciones-el%C3%A9ctricas-y-cables-en-el-sistema-de-protecci%C3%B3n-de.jpg?s=612x612&w=0&k=20&c=coWagFC8rVH3rgwqH0ksSrzit1sDvqBS-1yePuzH36c='),
        ('BMS', 'https://www.enelx.com/content/dam/local-argentina/automatizacion-1440x768.jpg'),
        ('Automotizaciones especiales', 'https://www.autycom.com/wp-content/uploads/2020/02/tendencias-de-automatizacion-industrial.jpg')
    ]

    return render_template('/clientes/Fermag/fermag.html', navBar = NavBar, servicios = Servicios)


@Fermag_home.route('/clientes/noticias')
def FermagNoticias():
    NavBar = getNavBar()
    Notis = [
        ('https://pbs.twimg.com/media/D6uc2kBX4AAv3xV.jpg', 'PRUEBA', 'Esto es una prueba pa ver si funca'),
        ('https://i.pinimg.com/236x/57/39/91/57399153da127ac6fe1d88512443bf3f.jpg', 'PRUEBAAA', 'Esto es una prueba pa ver si funcaaa'),
        ('http://pm1.narvii.com/7517/58894a30021ce56ed81b9dea917c7928d98e110dr1-958-811v2_uhq.jpg', 'PRUEBAAA', 'Esto es una prueba pa ver si funcaaa'),
        ('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv8lgDc1gGlVqn3UjDqKslOP6HrrUissH8xw&usqp=CAU', 'PRUEBAAAAAAA AAAAAAAAA', 'Esto es una prueba pa ver si funcaaaaa')
    ]
    return render_template('/clientes/Fermag/noticias.html', navBar = NavBar,notis = Notis)