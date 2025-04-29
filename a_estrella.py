"""Este es un ejemplo del algoritmo A*"""

import time
import heapq
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from node import Node

cities_mx = {
    "1":"Mexicali, Baja California, México", 
    "2":"La Paz, Baja California Sur, México",
    "3":"Chihuahua, Chihuahua, México",
    "4":"Saltillo, Coahuila, México",
    "5":"Durango, Durango, México",
    "6":"Monterrey, Nuevo León, México",
    "7":"San Luis Potosí, San Luis Potosí, México",
    "8":"Culiacán, Sinaloa, México", 
    "9":"Hermosillo, Sonora, México",
    "10":"Ciudad Victoria, Tamaulipas, México",
    "11":"Xalapa, Veracruz, México",
    "12":"Zacatecas, Zacatecas, México"
}

cities_edges={
    "1":{"2":1350, "9":744},
    "2":{"1":1350},
    "3":{"4":727,"5":631,"9":691},
    "4":{"3":727,"5":513,"6":85},
    "5":{"3":631,"4":513,"8":462,"12":289},        
    "6":{"4":85,"10":284,"12":462},
    "7":{"12":189},
    "8":{"5":462,"9":686},
    "9":{"1":744,"3":691,"8":686},
    "10":{"6":284,"11":706},
    "11":{"10":706},
    "12":{"5":289,"6":462,"7":189}
}

def get_distance(origin, goal):
    """
    Funcion para obtener la distancia entre dos ciudades dadas las claves (int) de cada ciudad

    Regresa la distancia en kilómetros entre las dos ciudades
    
    Si no se puede encontrar la distancia devuelve -1

    """
    locator = Nominatim(user_agent="a_estrella_DAMD")
    city1 = cities_mx[origin]
    city2 = cities_mx[goal]
    coordenates1 = locator.geocode(city1)
    time.sleep(1)
    coordenates2 = locator.geocode(city2)

    if city1 and city2:
        location1 = (coordenates1.latitude, coordenates1.longitude)
        location2 = (coordenates2.latitude, coordenates2.longitude)

        distancia = geodesic(location1, location2).km

        #print(f"La distancia entre {city1} y {city2} es de {distancia:.2f} km")
        return distancia
    else:
        print("No se pudo obtener la distancia")
        return -1


def a_star(origin, goal):
    start = Node(city=origin,g=0,h=get_distance(origin, goal))
    pending = [(start.f, start.city, start.g)]
    visited = set()
    route = []
    total_distance = 0

    while pending:
        current = heapq.heappop(pending)
        route.append(cities_mx[current[1]])
        total_distance += current[2] #current[2] es la distancia g hasta ese nodo
        print(f"{cities_mx[current[1]]} , {total_distance}")
        visited.add(current)


        if current[1] == goal:
            return route

        for neighbor, distance in cities_edges[current[1]].items(): #current[1] es la clave int de la ciudad en el dict cities_edges
            if neighbor in visited:
                continue  #skips already visited nodes

            # new_g = total_distance + distance #distance from start to neighbor

            new_neighbor = Node(city=neighbor, g = distance, h = get_distance(neighbor, goal))
            aux = (new_neighbor.f,new_neighbor.city, new_neighbor.g)
            if aux not in pending:
                heapq.heappush(pending, aux)

    return []


def main():
    for key, city in cities_mx.items():
        print(f"{key} - {city}")
    origin = input("Seleccione el origen (número): ")
    goal = input("Seleccione el destino (número): ")

    # get_distance(origin, goal)
    print(a_star(origin, goal))

main()
