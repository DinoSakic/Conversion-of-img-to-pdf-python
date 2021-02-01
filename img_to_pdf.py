from PIL import Image as Img
from glob import glob

# za pravilan raspored slika u pdf-u potrebno je slike numerirati na nacin:01,02,03...,10,11,....
ime_pdfa = ''
path = r''

def konvertuj(ime_pdfa,path):
    try:
        path = path + '\\*.jpg'
        ime_pdfa = ime_pdfa + '.pdf'
        lista_slika = [Img.open(slika) for slika in glob(path)]
        lista_slika[0].save(ime_pdfa,resolution=100.0, save_all=True, append_images=lista_slika[1:])
    except IndexError:
        print('GRESKA! \nVjerovatno je los path (mora postojati barem jedna slika u folderu)')

konvertuj(ime_pdfa,path)
