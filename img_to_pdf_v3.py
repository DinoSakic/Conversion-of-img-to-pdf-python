# _v2 rijesen problem sortiranja
# _v3 rijesen problem sa RGBA slikama

from PIL import Image as Img
import os
from natsort import natsorted

IME_PDFA = '' + '.pdf'
LOKACIJA_FAJLA = r''


def konvertuj(ime_pdfa, path):
    try:
        slike = []
        indeks = []
        ektenzija = ['.jpg', '.jpeg', '.bmp', '.img', '.png']
        filelist = natsorted(os.listdir(path))

        for idx, file in enumerate(filelist):
            name, ext = os.path.splitext(file)
            if ext in ektenzija:
                slike.append(path + '\\' + name + ext)  # jednostavnije je slike.append(file) al eto
            if ext == '.png':  # vjerovatno postoji bolji nacin
                indeks.append(idx)
        lista_slika = [Img.open(slika) for slika in slike]

# problem nastaje sa .png slikama koje su RGBA format. Ne mogu se direktno pretvoriti u pdf, zato je ovako skarabudzeno
        for kvaka22 in indeks:  # ovo je brze od: lista_slika = [slika.convert('RGB') for slika in lista_slika]
            lista_slika[kvaka22] = lista_slika[kvaka22].convert('RGB')

        lista_slika[0].save(ime_pdfa, color='RGB', resolution=100.0, save_all=True, append_images=lista_slika[1:])

    except IndexError:
        print('GRESKA! \nVjerovatno je los path (mora postojati barem jedna slika u folderu)')
    except PermissionError:
        print('Fajl mora biti zatvoren da bi mogao biti overwrite-an.')


konvertuj(IME_PDFA, LOKACIJA_FAJLA)
