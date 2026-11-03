"""Extrae las métricas reales de un ZIP de evidencias descargado de Colab."""
from pathlib import Path
from zipfile import ZipFile
import sys

def main(zip_path, output_dir='evidencias_colab'):
    out=Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    with ZipFile(zip_path) as z:
        for member in z.infolist():
            path=Path(member.filename)
            if path.is_absolute() or '..' in path.parts: raise ValueError('Ruta insegura en ZIP')
            z.extract(member,out)
    print('Archivos extraídos en',out)

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Uso: python src/extraer_evidencias.py evidencias_NBO_Amazon_v8.zip')
    main(sys.argv[1])
