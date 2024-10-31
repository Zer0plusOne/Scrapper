import os
import sys
import json
import csv
import xml.etree.ElementTree as ET # my house, my cellphone
from PIL import Image
import piexif
import PyPDF2
from mutagen import File
from docx import Document

#####################################################################
##   HAVE IN MIND I'M SPANISH SO I USE SPANISH WORDS IN MY CODE    ##
##                      made by: Zer0plusOne                       ##
#####################################################################


def extraer_metadatos_imagen(ruta_imagen):
    try:
        imagen = Image.open(ruta_imagen)
        exif_data = piexif.load(imagen.info['exif'])
        print("Metadata of the image:")
        for clave, valor in exif_data.items():
            print(f"{clave}: {valor}")
    except Exception as e:
        print(f"Error, metadata not found: {e}")

def extraer_metadatos_pdf(ruta_pdf):
    try:
        with open(ruta_pdf, 'rb') as archivo:
            lector = PyPDF2.PdfFileReader(archivo)
            metadatos = lector.getDocumentInfo()
            print("Metadata of the PDF:")
            for clave, valor in metadatos.items():
                print(f"{clave}: {valor}")
    except Exception as e:
        print(f"Error, metadata not found: {e}")

def extraer_metadatos_audio(ruta_audio):
    try:
        audio = File(ruta_audio)
        print("Metadata of the audio:")
        for clave, valor in audio.items():
            print(f"{clave}: {valor}")
    except Exception as e:
        print(f"Error, metadata not found: {e}")

def extraer_metadatos_word(ruta_docx):
    try:
        doc = Document(ruta_docx)
        propiedades = doc.core_properties
        print("Metadata of the document:")
        for clave, valor in propiedades.__dict__.items():
            print(f"{clave}: {valor}")
    except Exception as e:
        print(f"Error, metadata not found: {e}")

def guardar_metadatos(metadatos, formato_salida):
    if formato_salida == 'json':
        with open('metadata.json', 'w') as json_file:
            json.dump(metadatos, json_file, indent=4)
    elif formato_salida == 'csv':
        with open('metadata.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for clave, valor in metadatos.items():
                writer.writerow([clave, valor])
    elif formato_salida == 'xml':
        root = ET.Element("Metadatos")
        for clave, valor in metadatos.items():
            item = ET.SubElement(root, clave)
            item.text = str(valor)
        tree = ET.ElementTree(root)
        tree.write("metadata.xml")
    elif formato_salida == 'txt':
        with open('metadata.txt', 'w') as txt_file:
            for clave, valor in metadatos.items():
                txt_file.write(f"{clave}: {valor}\n")
    else:
        print("Format not supported, use json, csv, xml, or txt.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 Scrapper.py <archive> [-o <format>]")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    formato_salida = None

    if len(sys.argv) == 4 and sys.argv[2] == '-o':
        formato_salida = sys.argv[3].lower()

    if not os.path.isfile(ruta_archivo):
        print(f"Archive {ruta_archivo} not found, does not exist or is not reachable.")
        sys.exit(1)

    extension = os.path.splitext(ruta_archivo)[1].lower()
    metadatos = {}

    if extension in ['.jpg', '.jpeg', '.png']:
        metadatos = extraer_metadatos_imagen(ruta_archivo)
    elif extension == '.pdf':
        metadatos = extraer_metadatos_pdf(ruta_archivo)
    elif extension in ['.mp3', '.wav', '.flac']:
        metadatos = extraer_metadatos_audio(ruta_archivo)
    elif extension == '.docx':
        metadatos = extraer_metadatos_word(ruta_archivo)
    else:
        print("Archive not supported.")
        sys.exit(1)

    # Imprimir metadatos en consola
    print(metadatos)

    # Guardar metadatos en el formato solicitado
    if formato_salida:
        guardar_metadatos(metadatos, formato_salida)

if __name__ == "__main__":
    main()