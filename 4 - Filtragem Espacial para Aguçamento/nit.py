# -*- coding: utf-8 -*-
#python nit.py noisy_fingerprint.tif noisy_fingerprint_NIT.tif
#Digite: python nit.py <img_entrada> <img_saida>

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,color,util
import scipy.misc
from scipy.ndimage import filters 

np.seterr(divide='ignore', invalid='ignore')

def verificaDiretorio(diretorio):
    url = "/".join(diretorio.split('/')[:-1])
    if not os.path.isdir(url): # vemos de este diretorio ja existe
        os.mkdir(url) # aqui criamos a pasta caso nao exista
    if not os.path.isdir(diretorio):
        os.mkdir(diretorio)
        print ('Pasta criada com sucesso!')
    print("Diretório ok!")

pasta = "/".join( os.path.abspath(__file__).replace('\\','/').split('/')[:-1] ) +'/img_saida/'+ os.path.basename(__file__).split('.',1)[0]

#carrega a img1.tiff
img_1 = data.imread(sys.argv[1])
nome_img_saida = sys.argv[2]

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1)

#processa a imagem
k = 1
img_blurred = filters.gaussian_filter(img_1, sigma=5)
masc_nitidez = img_1 - img_blurred
img_nitidez = img_1 + k * masc_nitidez

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, img_nitidez)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(2,2,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(2,2,2)
plt.title("Imagem 3 - Borrada")
plt.imshow(img_blurred, cmap="gray")
plt.axis('off')

plt.subplot(2,2,3)
plt.title("Imagem 4 - Mascara de nitidez")
plt.imshow(masc_nitidez, cmap="gray")
plt.axis('off')

plt.subplot(2,2,4)
plt.title("Imagem 5 - Aplicacao da mascara de nitidez")
plt.imshow(img_nitidez, cmap="gray")
plt.axis('off')

plt.show()