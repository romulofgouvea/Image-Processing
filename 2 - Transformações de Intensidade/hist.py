# -*- coding: utf-8 -*-
#python python hist.py noisy_fingerprint.tif
#Digite: python aritm.py <img_entrada_1> <img_entrada_2> <img_saida>

import sys
import matplotlib.pyplot as plt
from skimage import data,color,util,exposure
 
img_1 = data.imread(sys.argv[1])

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1)

#processa a imagem
img_hist = exposure.histogram(img_1)

#Verificando a imagem através do plot
plt.figure()
plt.subplot(1,2,1)
plt.title("Imagem 1 - Original")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(1,2,2)
plt.hist(img_hist, bins=256, range=(0,255))
plt.title('Imagem 2 - Histograma nao normalizado.')
plt.axis('off')

plt.show()



    