# -*- coding: utf-8 -*-
#python lim_it.py noisy_fingerprint.tif noisy_fingerprint_LIM_IT.tif <T_ini>
#Digite: python lim_it.py <img_entrada> <img_saida> <T_ini>

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,color,util
import scipy.misc
from scipy.ndimage import filters 

np.seterr(divide='ignore', invalid='ignore')

def limiar_global_simples(im, T_ini=None, min_delta_T=None, plot=False):
    if T_ini==None:
        T_ini = im.mean()
    if min_delta_T==None:
        min_delta_T = im.max() * 0.001
    T = T_ini
    delta_T = np.inf

    i = 0
    while delta_T >= min_delta_T:
        g_bw = im > T
        num_px_bg, num_px_fg = np.bincount(g_bw.flatten())
        g_fg = im * g_bw
        g_bg = im * np.invert(g_bw)
        fg_mean = g_fg.sum() / float( num_px_fg )
        bg_mean = g_bg.sum() / float( num_px_bg )
        T_old = T
        T = 0.5 * (fg_mean + bg_mean)
        delta_T = np.abs(T - T_old)
        print('\nIteracao: ', i)
        print(' - T anterior: ', T_old)
        print(' - T atual: ' , T)
        print(' - delta_T: ', delta_T)
        i = i + 1

        if plot == True:

            plt.figure()
            plt.subplot(221)
            plt.imshow(im, cmap='gray')
            plt.title('Imagem original')
            plt.colorbar()
            plt.subplot(222)
            plt.imshow(g_bw, cmap='gray')
            plt.title('Imagem segmentada.')
            plt.colorbar()
            plt.subplot(223)
            plt.imshow(g_fg, cmap='gray')
            plt.colorbar()
            plt.title('Pixels de objeto.')
            plt.subplot(224)
            plt.imshow(g_bg, cmap='gray')
            plt.colorbar()
            plt.title('Pixels de fundo.')
            plt.show()

        return T

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
t_ini = float(sys.argv[3])

# Se necessário, converte para imagem em níveis de cinza.
if img_1.ndim > 2:
    img_1 = color.rgb2gray(img_1)

# Converte imagem para float.
img_1 = util.img_as_float(img_1.astype(np.uint8))

#processa a imagem
v_limiar = limiar_global_simples(img_1, t_ini)
im_bw = img_1 > v_limiar

#verifica o diretório
verificaDiretorio(pasta)

#salva na pasta com o nome especificado no comando
scipy.misc.imsave(pasta+'/'+nome_img_saida, im_bw)

#Verificando a imagem através do plot
plt.subplot(1,2,1)
plt.imshow(img_1, cmap='gray', interpolation='none')
plt.title('Imagem 1 - Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(im_bw, cmap='gray', interpolation='none')
plt.title('Imagem 2 - Segmentada por Limiarizacao iterativa')
plt.axis('off')

plt.show()