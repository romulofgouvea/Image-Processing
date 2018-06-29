# -*- coding: utf-8 -*-
#python aritm.py noisy_fingerprint.tif noisy_fingerprint_ARITM.tif
#Digite: python logic.py <img_entrada_1> <img_entrada_2> <img_saida>

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,color,util
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
img_2 = data.imread(sys.argv[2])
nome_img_saida = sys.argv[3]

#pega o caminho do computador até a pasta
pasta = "/".join( os.path.abspath(__file__).replace('\\','/').split('/')[:-1] ) +'/img_saida/'+ os.path.basename(__file__).split('.',1)[0]

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

if img_2.ndim > 2:
    img_2 = color.rgb2gray(img_2)

#processa as imagens
img_and = np.logical_and(img_1,img_2)
img_or = np.logical_or(img_1,img_2)

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, img_and)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(2,3,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_and, cmap="gray")
plt.axis('off')

plt.subplot(2,3,4)
plt.title("Imagem 2 - Original")
plt.imshow(img_2, cmap="gray")
plt.axis('off')

plt.subplot(2,3,2)
plt.title("Imagem 3 - Usando operador And")
plt.imshow(img_and, cmap="gray")
plt.axis('off')


plt.subplot(2,3,3)
plt.title("Or")
plt.imshow(img_or, cmap="gray")
plt.axis('off')

plt.show()