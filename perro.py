
perro = {}

perro["nombre"]="mia"
perro["color"]="blanca"
perro["raza"]="chihuahua"
perro["patas"]="4"
perro["edad"]="2"

estudiante = {"nombre":"yajaira",
  "apellido":"rodriguez",
  "sexo":"femenino",
  "edad":"18",
  "estado civil":"soltera",
  "habilidades":["rapidez, inteligencia"],
  "pais":"colombia",
  "cuidad":"cartagena",
  "direcion":"chiquinquira m43 l2"
}

print(estudiante)
print(len(perro))
print(estudiante["habilidades"])
estudiante["habilidades"].append("vision")
print(estudiante["habilidades"])
keys=estudiante.keys()
print(keys)
values=estudiante.values()
print(values)
print(estudiante.items())
estudiante.pop("edad")
print(estudiante)
print(estudiante.clear())




  
  




