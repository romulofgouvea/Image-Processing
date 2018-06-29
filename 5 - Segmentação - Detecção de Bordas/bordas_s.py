# -*- coding: utf-8 -*-
#python bordas_s.py noisy_fingerprint.tif noisy_fingerprint_BORDAS_S.tif 5
#Digite: python grad.py <img_entrada> <img_saida>

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

img = img_1
img_1 = filters.convolve(img_1, masc_random, mode='constant', cval=0)

# Operadores de Sobel
sob_h = np.array([[-1., -2., -1.],
                  [ 0.,  0.,  0.],
                  [ 1.,  2.,  1.]], dtype=float)
sob_v = np.array([[-1.,  0.,  1.],
                  [-2.,  0.,  2.],
                  [-1.,  0.,  1.]], dtype=float)

# Gradiente de Sobel.
im_sob_h  = filters.convolve(img_1, sob_h)
im_sob_v  = filters.convolve(img_1, sob_v)

# Magnitude do gradiente (hipotenusa)
im_sob = np.sqrt(im_sob_h**2 + im_sob_v**2)

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, im_sob)

#Verificando a imagem através do plot
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray', interpolation='none')
plt.title('Imagem 1 - Original')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(im_sob, cmap='gray', interpolation='none')
plt.title('Imagem 2 - Gradiente de Sobel - Exato (hipotenusa)')
plt.axis('off')

# - linha 2
plt.subplot(2,2,3)
plt.imshow(img_1[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Imagem 3 - Gradiente de Sobel - Original')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(im_sob[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Imagem 4 - Gradiente de Sobel - Final')
plt.axis('off')

plt.show()