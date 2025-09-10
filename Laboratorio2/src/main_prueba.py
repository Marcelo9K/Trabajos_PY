from pathlib import Path
from def_prueba import procesar_csv, calcular_kpis


# --- Configuración de rutas ---
ROOT = Path(__file__).resolve().parents[2]   # carpeta actual
TXT  = ROOT / "Laboratorio2"
IN_FILE  = TXT / "datos" / "raw" / "datos_sucios_250_v2.csv"
OUT_FILE = TXT / "datos" / "proccesing" / "Temperaturas_Procesado.csv"


def main():
    # Procesar archivo CSV
    total, kept, empty_val, bad_ts, voltajes, temperaturas = procesar_csv(IN_FILE, OUT_FILE)

    # Calcular KPIs
    kpis, kpis_calidad = calcular_kpis(voltajes, temperaturas, total, kept, empty_val, bad_ts)

    # Mostrar resultados
    print("=== KPIs de Temperatura ===")
    if kpis["n"] == 0:
        print("No se encontraron datos válidos.")
    else:
        print(f"Cantidad de datos válidos: {kpis['n']}")
        print(f"Temperatura mínima: {kpis['min']:.2f} °C")
        print(f"Temperatura máxima: {kpis['max']:.2f} °C")
        print(f"Promedio: {kpis['prom']:.2f} °C")
        print(f"Alertas (>40°C): {kpis['alerts']}")

    print("\n=== KPIs de Calidad de Datos ===")
    print(f"Filas totales: {kpis_calidad['filas_totales']}")
    print(f"Filas válidas: {kpis_calidad['filas_validas']}")
    print(f"Descartes por valor: {kpis_calidad['descartes_valor']}")
    print(f"Descartes por timestamp: {kpis_calidad['descartes_timestamp']}")


if __name__ == "__main__":
    main()
