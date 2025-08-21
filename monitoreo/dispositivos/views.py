from django.shortcuts import render

def inicio(request):
    contexto = {"nombre": "Javiera"}
    productos = [
        {"nombre": "Sensor 1", "valor": 100},
        {"nombre": "Sensor 2", "valor": 200},
        {"nombre": "Sensor 3", "valor": 300},
    ]

    return render(request, "dispositivos/inicio.html", {
        "contexto": contexto,
        "productos": productos
    })

def panel_dispositivos(request):
    dispositivos = [
        {
        "nombre": "Sensor Temperatura",
        "consumo": 50,
        "limite": 100
        },

        {"nombre": "Medidor Solar",
         "consumo": 120,
         "limite": 100
        },

        {"nombre": "Sensor Movimiento",
         "consumo": 30,
         "limite": 100
        },

        {"nombre": "Calefactor",
         "consumo": 200,
         "limite": 150
        },
    ]

    print("=== DEBUG INICIO ===")
    print("Dispositivos:", dispositivos)  # ← Esto aparecerá en la TERMINAL
    print("=== DEBUG FIN ===")

    for dispositivo in dispositivos:
        if dispositivo['consumo'] > dispositivo ['limite']:
            dispositivo['estado']= 'Excede el límite'
            dispositivo['clase_css'] = 'rojo'
        else:
            dispositivo['estado'] = "Dentro del límite"
            dispositivo['clase_css'] = 'verde'
 
    consumo_maximo = 100

    return render(request, "dispositivos/panel.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": 100
    })