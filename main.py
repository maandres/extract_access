from database import insert

#PARAMETRES
domini_g = "54.172.36.38"
usuari_g = "pi"
contrasenya_g = "Fes44_"
base_dades_g = "soldatal2"
camps_g = "Id,nom"
taula_g = "operaris"
valors_g = "'eit','quetal'"

arguments = (domini_g,
             usuari_g,
             contrasenya_g,
             base_dades_g,             
             taula_g,
             camps_g,
             valors_g
            )

retorn = insert(*arguments)
print(retorn)