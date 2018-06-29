# -*- coding: utf-8 -*-
#python maxmin.py noisy_fingerprint.tif noisy_fingerprint_MIN.tif noisy_fingerprint_MAX.tif 3
#Digite: python maxmin.py <img_entrada> <img_saida_min> <imgsaida_max> <mask_size>

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
nome_img_saida1 = sys.argv[2]
nome_img_saida2 = sys.argv[3]
mask_size = int(sys.argv[4])

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1)

#processa a imagem
filtro_min = filters.minimum_filter(img_1,size=mask_size)
filtro_max = filters.maximum_filter(img_1,size=mask_size)

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida1, filtro_min)
scipy.misc.imsave(pasta+'/'+nome_img_saida2, filtro_max)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(1,3,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Imagem 2 - Filtro Min")
plt.imshow(filtro_min, cmap="gray")
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Imagem 3 - Filtro Max")
plt.imshow(filtro_max, cmap="gray")
plt.axis('off')

plt.show()