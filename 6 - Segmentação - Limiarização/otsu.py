# -*- coding: utf-8 -*-
#python otsu.py noisy_fingerprint.tif noisy_fingerprint_OTSU.tif
#Digite: python otsu.py <img_entrada> <img_saida>

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,color,util,filters
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

pasta = "/".join( os.path.abspath(__file__).replace('\\','/').split('/')[:-1] ) +'/img_saida/'+ os.path.basename(__file__).split('.',1)[0]

#carrega a img1.tiff
img_1 = data.imread(sys.argv[1])
nome_img_saida = sys.argv[2]

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
# img_1 = util.img_as_float(img_1)

#processa a imagem
t_otsu = filters.threshold_otsu(img_1)
im_otsu = img_1 < t_otsu

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, im_otsu)

#Verificando a imagem através do plot
plt.subplot(1,2,1)
plt.imshow(img_1, cmap='gray', interpolation='none')
plt.title('Imagem 1 - Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(im_otsu, cmap='gray', interpolation='none')
plt.title('Imagem 2 - Limiarizacao Otsu')
plt.axis('off')

plt.show()