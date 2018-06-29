# -*- coding: utf-8 -*-
#python media.py noisy_fingerprint.tif noisy_fingerprint_MEDIA.tif 5
#Digite: python media.py <img_entrada> <img_saida> <mask_size>

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
mask_size = int(sys.argv[3])

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1)

#processa a imagem
masc_random = np.ones([mask_size,mask_size], dtype=float)
masc_random = masc_random / float(mask_size^2)

filtro_media = filters.convolve(img_1, masc_random, mode='constant', cval=0)

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, filtro_media)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(1,2,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Imagem 2 - Filtro Media")
plt.imshow(filtro_media, cmap="gray")
plt.axis('off')

plt.show()