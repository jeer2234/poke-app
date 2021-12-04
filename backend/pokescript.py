#import argparse

#parser = argparse.ArgumentParser(description='Consultador de pokemons.')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    #help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',
                    #const=sum, default=max,
                    #help='sum the integers (default: find the max)')

#args = parser.parse_args()
#print(args.accumulate(args.integers))
import apicall
import requests
from pymongo import MongoClient


client = MongoClient("mongodb+srv://javier2234:7jzUUZXvFpon0q7Y@cluster0.bpm8m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",port=27017)
db=client.pokedata


aceptar = ['y','yes', 'YES','si','s','SI']
rechazar = ['n','no','NO']
user = input('ingresa tu nombre de entrenador pokemon: ')


player = db.trainers.find_one({'trainer': user})
print (player)


if player is None:

    db.trainers.insert_one(player)

    print(" bienvenido, veo que eres nuevo por aqui {}".format(user))
elif :
    print('bienvenido entrenador {} tus pokemon capturados son :'.format(user))
  
comenzar = input('quieres buscar pokemons?(Y/N): ')

if comenzar in rechazar:
    print('adios ')
elif comenzar in aceptar:
    inicio = True

    while inicio:
      
        search = input('ingresa el nombre del pokemon que buscas o su id en la pokedex: ')

        try:
            search = apicall._call_api_pokemon(search)

            
            aswer= input("has encontrado al pokemon {}, deseas capturarlo?(Y/N): ".format(search))


            if aswer in rechazar:
                    aswer2 = input('quieres seguir buscando mas pokemons?(Y/N): ')
                    if aswer2 in rechazar:
                        print('adios ')
                        break
                    elif aswer2 in aceptar:
                        pass
                    else :
                        print('respuesta no valida, intenta denuevo')

            elif aswer in aceptar:
                aswer3=None
                aswer3= input('pokemon capturado, quieres buscar otro pokemons?(Y/N): ')
                if aswer3 in rechazar:
                    print('adios ')
                    break
                elif aswer3 in aceptar:
                    pass
                else:
                     while aswer3 not in aceptar and aswer3 not in rechazar:
                        print('respuesta no valida, intenta denuevo')
                        aswer3= input('responde si o no, quieres buscar otro pokemons?(Y/N): ')
                        if aswer3 in rechazar:
                            print('adios ')
                            inicio=False
                            
                
                        
            else:
                print('respuesta no valida, intenta denuevo')
        except requests.exceptions.HTTPError:
            print("id o nombre de pokemon no encontrado en la pokedex, intenta denuevo")
else:
    print('respuesta no valida intenta de nuevo luego.')
