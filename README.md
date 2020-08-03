Para executar siga os seguintes passos:
- Coloque as imagens que deseja processar na pasta imagens
- Entre na pasta do script desejado pelo terminal
- Execute algo como: 
python <script.py> <imagem1.tif> <imagem2.tif> <nome de saida>
python logic.py img1.tiff img2.tiff noisy_fingerprint_LOGIC.tif

Para a execução de cada algoritmo execute uma linha existente para cada exemplo:

```bash
python aritm.py noisy_fingerprint.tif noisy_fingerprint_ARITM.tif

python logic.py noisy_fingerprint.tif noisy_fingerprint_LOGIC.tif

python neg.py noisy_fingerprint.tif noisy_fingerprint_NEG.tif

python gama.py noisy_fingerprint.tif noisy_fingerprint_GAMA.tif 0.5

python cont.py noisy_fingerprint.tif noisy_fingerprint_CONT.tif

python hist.py noisy_fingerprint.tif

python eq.py noisy_fingerprint.tif noisy_fingerprint_EQ.tif

python media.py noisy_fingerprint.tif noisy_fingerprint_MEDIA.tif 5

python gauss.py noisy_fingerprint.tif noisy_fingerprint_GAUSS.tif 15

python med.py noisy_fingerprint.tif noisy_fingerprint_MED.tif 5

python maxmin.py noisy_fingerprint.tif noisy_fingerprint_MIN.tif noisy_fingerprint_MAX.tif 3

python lap.py noisy_fingerprint.tif noisy_fingerprint_LAP.tif

python nit.py noisy_fingerprint.tif noisy_fingerprint_NIT.tif

python grad.py noisy_fingerprint.tif noisy_fingerprint_GRAD.tif

python bordas_s.py noisy_fingerprint.tif noisy_fingerprint_BORDAS_S.tif 5

python bordas_l.py noisy_fingerprint.tif noisy_fingerprint_BORDAS_L.tif 5

python lim_it.py noisy_fingerprint.tif noisy_fingerprint_LIM_IT.tif <T_ini>

python otsu.py noisy_fingerprint.tif noisy_fingerprint_OTSU.tif

python lim_s.py noisy_fingerprint.tif noisy_fingerprint_LIM_S.tif 5
```
