# -*- coding: utf-8 -*-
#python aritm.py noisy_fingerprint.tif noisy_fingerprint_ARITM.tif
import sys
import os.path
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
from skimage import data,color,util,exposure
import scipy.misc

img_1 = data.imread(sys.argv[1])

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1)


img_hist = exposure.histogram(img_1)

plt.figure()
plt.subplot(2,2,1)
plt.title("Imagem 1")
plt.imshow(img_1, cmap="gray")
plt.axis('off')

plt.subplot(2,2,2)
plt.hist(img_hist, bins=256, range=(0,255))
plt.title('Histograma nao normalizado.')
plt.axis('off')

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



    