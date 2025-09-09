from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TXT = ROOT / "Archivos"/ "mediciones_200_mixto.txt"

valores=[]
with open(TXT, 'r', encoding='"utf-8"') as f:
    for linea in f: 
        s=linea.strip()
        if not s or s.startswith("#"):
            continue
        if not s or s.startswith("!"):
            continue
        if not s or s.startswith(" "):
            continue
        s = s.replace(",", ".")
        try:
            valores.append(float(s))
        except ValueError:
            pass

print(valores)