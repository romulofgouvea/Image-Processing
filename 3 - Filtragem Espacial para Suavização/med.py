# -*- coding: utf-8 -*-
#python med.py noisy_fingerprint.tif noisy_fingerprint_MED.tif 5
#Digite: python med.py <img_entrada> <img_saida> <mask_size>

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

def carregaImg(arg):
    return data.imread("../imagens/"+arg)

#carrega imagem
img_1 = carregaImg(sys.argv[1])
nome_img_saida = sys.argv[2]
mask_size = int(sys.argv[3])

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1)

#processa a imagem
filtro_mediana = filters.median_filter(img_1, size=mask_size)

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, filtro_mediana)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(1,2,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Imagem 2 - Filtro Mediana")
plt.imshow(filtro_mediana, cmap="gray")
plt.axis('off')

plt.show()