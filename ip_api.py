import requests
import json
def consulta_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return {
            'query': data.get('query'),
            'pais': data.get('country'),
            'region': data.get('regionName'),
            'isp': data.get('isp'),
            'coordenadas': {
                'latitud': data.get('lat'),
                'longitud': data.get('lon')
            }
        }
    except Exception as e:
        print(f"Error al consultar {ip}: {e}")
        return None

def main():
    resultados = []
    while True:
        ip = input("Ingresa una IP pública (o 'exit' para salir): ").strip()
        if ip.lower() == 'exit':
            break
        info = consulta_ip(ip)
        if info:
            print(f"País: {info['pais']}")
            print(f"Región: {info['region']}")
            print(f"ISP: {info['isp']}")
            coords = info['coordenadas']
            print(f"Coordenadas: {coords['latitud']}, {coords['longitud']}")
            print('-' * 40)
            resultados.append(info)
    # Guardar resultados en archivo JSON
    with open('resultados_ips.json', 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)
    print("Resultados guardados en resultados_ips.json")

if __name__ == '__main__':
    main()
