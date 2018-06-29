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
img_blur_orig = filters.gaussian_filter(img_1, sigma=3)
img_blurred = filters.gaussian_filter(img_blur_orig, 3)

# Mascara
masc_nitidez = img_blur_orig - img_blurred

# Mascara de nitidez
k = 1
img_nitidez = img_blur_orig + k * masc_nitidez

# Teste valores de k (de 0.1 em 0.1) ate comecar a aparece valore negativos.
for k in np.arange(1.1,5.,0.1): # De 1.1 até 5.0, de 0.1  em 0.1!
    img_boost = img_blur_orig + k * masc_nitidez
    if img_boost.min() < 0:
        img_boost = img_blur_orig + k-0.1 * masc_nitidez
        break

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, img_boost)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(2,3,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(2,3,2)
plt.title("Imagem 2 - Original borrada")
plt.imshow(img_blur_orig, cmap="gray")
plt.axis('off')

plt.subplot(2,3,3)
plt.title("Imagem 3 - Borrada")
plt.imshow(img_blurred, cmap="gray")
plt.axis('off')

plt.subplot(2,3,4)
plt.title("Imagem 4 - Mascara de nitidez")
plt.imshow(masc_nitidez, cmap="gray")
plt.axis('off')

plt.subplot(2,3,5)
plt.title("Imagem 5 - Aplicacao da mascara de nitidez")
plt.imshow(img_nitidez, cmap="gray")
plt.axis('off')

plt.subplot(2,3,6)
plt.title("Imagem 6 - Filtro high-boost")
plt.imshow(img_boost, cmap="gray")
plt.axis('off')

plt.show()