import mysql.connector as mysql

#PARAMETRES
domini_g = "54.172.36.38"
usuari_g = "pi"
contrasenya_g = "Fes44_"
base_dades_g = "soldatal2"
camps_g = "Id,nom"
taula_g = "operaris"


def insert(domini,usuari,contrasenya,base_dades,taula,camps,valors):
  #Ens conectem a la base de dades
  db = mysql.connect(host=domini, user=usuari, passwd=contrasenya,database=base_dades)
  cursor = db.cursor()
  query = "INSERT INTO "+ taula + " (" + camps +") VALUE (" + valors + ")"
  cursor.execute(query)
  db.commit()
  
  cursor.close()
  db.close()
  
  print("Fi de  la incserció")
  return "insert ok"

def select(domini,usuari,contrasenya,base_dades,camps,taula):
  db = mysql.connect(host=domini, user=usuari, passwd=contrasenya,database=base_dades)

  cursor = db.cursor()

  query = "SELECT "+ camps +" FROM " + taula
  cursor.execute(query)
  resultado = cursor.fetchall()
  db.commit()

  print(resultado)

  cursor.close()
  db.close()
  print("Fi de la selecció")
  return "select ok"
#SELECT
#Exemple de select

def main():
  arguments = (domini_g,
               usuari_g,
               contrasenya_g,
               base_dades_g,
               camps_g,
               taula_g
              )
  
  retorn = select(*arguments)
  print(retorn)

if __name__=="__main__":
  main()