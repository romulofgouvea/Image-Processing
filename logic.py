# -*- coding: utf-8 -*-
#python aritm.py noisy_fingerprint.tif noisy_fingerprint_ARITM.tif
import sys
import os.path
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
from skimage import data,color,util
import scipy.misc

def verificaDiretorio(diretorio):
    url = diretorio.split('/',1)
    if (not os.path.isdir(url[0])): # vemos de este diretorio ja existe
        os.mkdir(url[0]) # aqui criamos a pasta caso nao exista
    if os.path.isdir(diretorio):
        print ('Arquivo salvo no diretorio: '+ diretorio[1])
    else:
        os.mkdir(diretorio)
        print ('Pasta criada com sucesso!')

#carrega a img1.tiff
img_1 = data.imread(sys.argv[1])
img_2 = data.imread(sys.argv[2])

pasta = 'img_saida/logic'

try:
    pasta = sys.argv[3]
except (IndexError):
    print('\nO diretorio padrao e '+pasta+'para alterar envie o caminho da nova pasta!')
    print('Digite: python aritm.py img1.tiff img2.tif C:\Users\Romulo Fernandes\Desktop \n')

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

if img_2.ndim > 2:
    img_2 = color.rgb2gray(img_2)

# Converte imagem para float.
img_1 = util.img_as_bool(img_1)
img_2 = util.img_as_bool(img_2)

img_and = np.logical_and(img_1,img_2)
img_or = np.logical_or(img_1,img_2)
    
verificaDiretorio(pasta)

scipy.misc.imsave(pasta+'/img_and.jpg', img_and)
# plt.figure()
# plt.subplot(2,3,1)
# plt.title("Imagem 1 - Original")
# plt.imshow(img_and, cmap="gray")
# plt.axis('off')

# plt.subplot(2,3,4)
# plt.title("Imagem 2 - Original")
# plt.imshow(img_2, cmap="gray")
# plt.axis('off')

# plt.subplot(2,3,2)
# plt.title("And")
# plt.imshow(img_and, cmap="gray")
# plt.axis('off')


# plt.subplot(2,3,3)
# plt.title("Or")
# plt.imshow(img_or, cmap="gray")
# plt.axis('off')

# plt.show()