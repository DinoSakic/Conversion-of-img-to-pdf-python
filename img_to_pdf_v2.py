# _v2 rijesen problem sortiranja

from PIL import Image as Img
import os
from natsort import natsorted

Ime_pdfa = ''
lokacija_fajla = r''


def konvertuj(ime_pdfa, path):
    try:
        pdf = ime_pdfa + '.pdf'
        slike = []
        filelist = natsorted(os.listdir(path))
        ektenzija = ['.jpg', '.jpeg', '.png', '.bmp', '.img']
        for file in filelist:
            name, ext = os.path.splitext(file)
            if ext in ektenzija:
                slike.append(path + '\\' + name + ext)
        lista_slika = [Img.open(slika) for slika in slike]
        lista_slika[0].save(pdf, resolution=100.0, save_all=True, append_images=lista_slika[1:])
    except IndexError:
        print('GRESKA! \nVjerovatno je los path (mora postojati barem jedna slika u folderu)')


konvertuj(Ime_pdfa, lokacija_fajla)
