# -*- coding: utf-8 -*-
#python aritm.py noisy_fingerprint.tif noisy_fingerprint_ARITM.tif
import sys
import os.path
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
from skimage import data,color,util,exposure
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

pasta = 'img_saida/cont'

#carrega a img1.tiff
img_1 = data.imread(sys.argv[1])

try:
    pasta = sys.argv[2]
except (IndexError):
    print('\nO diretorio padrao e '+pasta+'para alterar envie o caminho da nova pasta!')
    print('Digite: python aritm.py img1.tiff img2.tif C:\Users\Romulo Fernandes\Desktop \n')

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1)

# Alargamento de contraste 1.
img_cont1 = exposure.rescale_intensity(img_1)
# Alargamento de contraste 2
img_cont2 = exposure.rescale_intensity(img_1, (0.2,0.6), (0.0,1.0))

verificaDiretorio(pasta)

scipy.misc.imsave(pasta+'/img_cont2.jpg', img_cont2)

plt.figure()
plt.subplot(2,3,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_cont2, cmap="gray")
plt.axis('off')

# plt.subplot(2,3,4)
# plt.title("Imagem 2 - Original")
# plt.imshow(img_2, cmap="gray")
# plt.axis('off')

# plt.subplot(2,3,2)
# plt.title("Soma")
# plt.imshow(img_som, cmap="gray")
# plt.axis('off')


# plt.subplot(2,3,3)
# plt.title("Subtracao")
# plt.imshow(img_sub, cmap="gray")
# plt.axis('off')

# plt.subplot(2,3,5)
# plt.title("Mutiplicacao")
# plt.imshow(img_mult, cmap="gray")
# plt.axis('off')

# plt.subplot(2,3,6)
# plt.title("Divisao")

# plt.imshow(img_div , cmap="gray")
# plt.axis('off')

plt.show()



    