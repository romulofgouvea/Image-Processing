# -*- coding: utf-8 -*-
#python cont.py noisy_fingerprint.tif noisy_fingerprint_CONT.tif
#Digite: python cont.py <img_entrada> <img_saida>

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,color,util,exposure
import scipy.misc

np.seterr(divide='ignore', invalid='ignore')

def verificaDiretorio(diretorio):
    url = "/".join(diretorio.split('/')[:-1])
    if not os.path.isdir(url): # vemos de este diretorio ja existe
        os.mkdir(url) # aqui criamos a pasta caso nao exista
    if not os.path.isdir(diretorio):
        os.mkdir(diretorio)
        print ('Pasta criada com sucesso!')
    print("Diretório ok!")

#carrega a img1.tiff
img_1 = data.imread(sys.argv[1])
nome_img_saida = sys.argv[2]

#pega o caminho do computador até a pasta
pasta = "/".join( os.path.abspath(__file__).replace('\\','/').split('/')[:-1] ) +'/img_saida/'+ os.path.basename(__file__).split('.',1)[0]

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

img_1 = util.img_as_float(img_1)

# Alargamento de contraste 1.
img_cont1 = exposure.rescale_intensity(img_1)
# Alargamento de contraste 2
img_cont2 = exposure.rescale_intensity(img_1, (0.2,0.6), (0.0,1.0))

verificaDiretorio(pasta)

scipy.misc.imsave(pasta+'/'+nome_img_saida, img_cont2)

plt.figure()
plt.subplot(1,3,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Imagem 2 - Contraste 1")
plt.imshow(img_cont1, cmap="gray")
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Imagem 3 - Contraste 2")
plt.imshow(img_cont2, cmap="gray")
plt.axis('off')

plt.show()