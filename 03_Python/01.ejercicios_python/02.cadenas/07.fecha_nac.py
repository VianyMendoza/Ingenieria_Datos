def cumple (fecha_nac):
    dic_mes ={
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzoo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre"   
    }
    
    
    dia = fecha_nac[:fecha_nac.find("/"):]
    mes = fecha_nac[fecha_nac.find("/")+1:fecha_nac.rfind("/"):]
    año = fecha_nac[fecha_nac.rfind("/")+1::]
    
    print(f"Día de nacimiento {dia}")
    print(f"Del mes de {dic_mes.get(mes)}")
    print(f"Del año {año}")

print(cumple(input("¿Cuándo es tu cumpleaños? (dd/mm/aaaa)\n")))