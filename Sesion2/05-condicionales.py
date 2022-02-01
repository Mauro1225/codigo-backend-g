personas = [
    { 
    'nombre':'Adriana',
    'edad':25
    },
    {
    'nombre':'Nicolas',
    'edad':15
    },
    {
    'nombre':'Maria',
    'edad':23
    },
    {
    'nombre':'Guillermo',
    'edad':18
    }
]
personas_mas_de_20=0
personas_menos_de_20= 'Las personas son: '

for persona in personas:
    if(persona['edad']>20):
        personas_mas_de_20 += 1
    else:
        personas_menos_de_20 += persona['nombre']+' '

print('Hay', personas_mas_de_20,' personas con más de 20 años')

print(personas_menos_de_20)
