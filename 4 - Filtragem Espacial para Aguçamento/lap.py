# -*- coding: utf-8 -*-
#python lap.py noisy_fingerprint.tif noisy_fingerprint_LAP.tif
#Digite: python lap.py <img_entrada> <img_saida>

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
# Mascaras - Laplaciano 4
lap_4 = np.array([[ 0.,  1., 0.],
                  [ 1., -4., 1.],
                  [ 0.,  1., 0.]], dtype=float)


# Calcula os imagens filtradas pelas máscaras laplacianas
im_lap_4 = filters.convolve(img_1, lap_4)

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, im_lap_4)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(1,2,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Imagem 2 - Laplaciano")
plt.imshow(im_lap_4, cmap="gray")
plt.axis('off')

plt.show()