import csv
from datetime import datetime
from statistics import mean


def procesar_csv(in_file, out_file):
    """
    Lee un CSV de entrada, limpia los datos y escribe un CSV de salida con:
    - Timestamp en formato ISO YYYY-MM-DDTHH:MM:SS
    - Voltaje con 2 decimales
    - Temp_C con 2 decimales
    - Columna de Alertas
    """

    with open(in_file, "r", encoding="utf-8", newline="") as fin, \
         open(out_file, "w", encoding="utf-8", newline="") as fout:

        reader = csv.DictReader(fin, delimiter=";")
        writer = csv.DictWriter(fout, fieldnames=["Timestamp", "Voltaje", "Temp_C", "Alertas"])
        writer.writeheader()

        total = kept = 0
        empty_val = bad_ts = 0
        voltajes = []
        temperaturas = []

        for row in reader:
            total += 1
            ts_raw = (row.get("timestamp") or "").strip()
            val_raw = (row.get("value") or "").strip()

            # limpiar valores numéricos
            val_raw = val_raw.replace(",", ".")
            if val_raw.lower() in {"", "na", "n/a", "nan", "null", "none", "error"}:
                empty_val += 1
                continue

            try:
                val = float(val_raw)
            except ValueError:
                empty_val += 1
                continue

            # limpiar timestamp
            ts_clean = None
            for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
                try:
                    dt = datetime.strptime(ts_raw, fmt)
                    ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                    break
                except ValueError:
                    pass

            if ts_clean is None and "T" in ts_raw and len(ts_raw) >= 19:
                try:
                    dt = datetime.strptime(ts_raw[:19], "%Y-%m-%dT%H:%M:%S")
                    ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                except ValueError:
                    ts_clean = None

            if ts_clean is None:
                bad_ts += 1
                continue

            # transformar voltaje a temperatura
            temp = 18 * val - 64
            control = "ALERTA" if temp > 40 else "OK"

            voltajes.append(val)
            temperaturas.append(temp)

            # escribir fila limpia en archivo de salida
            writer.writerow({
                "Timestamp": ts_clean,
                "Voltaje": f"{val:.2f}",
                "Temp_C": f"{temp:.2f}",
                "Alertas": control
            })

            kept += 1

    return total, kept, empty_val, bad_ts, voltajes, temperaturas


def calcular_kpis(voltajes, temperaturas, total, kept, empty_val, bad_ts):
    """
    Calcula KPIs de datos procesados y calidad.
    """
    n = len(voltajes)
    if n == 0:
        kpis = {"n": 0, "min": None, "max": None, "prom": None, "alerts": 0}
    else:
        alertas = sum(temp > 40 for temp in temperaturas)
        kpis = {
            "n": n,
            "min": min(temperaturas),
            "max": max(temperaturas),
            "prom": mean(temperaturas),
            "alerts": alertas,
        }

    kpis_calidad = {
        "filas_totales": total,
        "filas_validas": kept,
        "descartes_timestamp": bad_ts,
        "descartes_valor": empty_val,
    }

    return kpis, kpis_calidad