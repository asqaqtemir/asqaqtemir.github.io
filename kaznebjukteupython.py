import os
import requests
from PIL import Image
from io import BytesIO
from fpdf import FPDF

# pip install requests - для скачивания данных по URL
# pip install Pillow - для работы с изображениями
# pip install fpdf - для создания PDF документов

# python .\kazneb.py     python .\kazneb.py       python .\kazneb.py     python .\kazneb.py





# Многострочная строка с URL-ами-----------------------------------------------------------------------
image_urls = '''

https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0001.png?time=1737840592857&key=c89c14391b9d95dce69bad6f88f9bc74
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0002.png?time=1737840592857&key=61fa1b901f2313516bc2ff0ee9087c55
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0003.png?time=1737840592857&key=abc84d42e6c5c7779aec4ee1894e4657
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0004.png?time=1737840592857&key=b6f9e71f61778de905fdfca9f99edd33
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0005.png?time=1737840592857&key=4aaf219286957e8312d96c263337d244
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0006.png?time=1737840592857&key=2deb2e69e6b57e11b95b9ee29491a357
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0007.png?time=1737840592857&key=616f890c48c7f8e971b9b852cd572fb5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0008.png?time=1737840592857&key=d04e190c72024e7cac0256fd2e807b79
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0009.png?time=1737840592857&key=223fc435f2ebace4cfe05aa68dd26bec
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0010.png?time=1737840592857&key=fa5a421c29f470d9c82fc8290000d476
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0011.png?time=1737840592857&key=9c08699725010a3ea10fa013956b30ac
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0012.png?time=1737840592857&key=6945f6e4fc78df7b7dbc379877777d9b
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0013.png?time=1737840592857&key=5da0a7920af3b84244da3f2efa19afe3
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0014.png?time=1737840592857&key=071fad558eb021f62d16bd2bfed062d6
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0015.png?time=1737840592857&key=b8c753f4d0054083698508991e9947a4
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0016.png?time=1737840592857&key=a0a60cb0bade246e62e04304216ce6f9
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0017.png?time=1737840592857&key=b67c21787eb2be2d0134c4c4c604f445
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0018.png?time=1737840592857&key=48d4451d727600a5a8d387a5af009623
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0019.png?time=1737840592857&key=1079f2dbd03e5a7b286a9c6170890c8d
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0020.png?time=1737840592857&key=48e79e279e42ddd9dd66c5533117c348
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0021.png?time=1737840592857&key=3c7538384b2f98fe9ee766b163e82ba6
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0022.png?time=1737840592857&key=215f6c933e05cdc04413097df7236cd5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0023.png?time=1737840592857&key=b474e316fa9959920e798750899a9fa9
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0024.png?time=1737840592857&key=762b8b058d5fb8c53a2f42cc7ebab999
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0025.png?time=1737840592857&key=f9ce21999639b7a743e080aab059d06e
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0026.png?time=1737840592857&key=b243aa79d368e648e879573c114a3aa5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0027.png?time=1737840592857&key=d2579ca93fcf37caf502f809071d9c7d
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0028.png?time=1737840592857&key=a1748fd75cc67a8e1117c4f873280ab4
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0029.png?time=1737840592857&key=f82fea2dd68fe457a3433898cc344dd9
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0030.png?time=1737840592857&key=777b8105f4a2c8ddc48c9c33cc58a37c
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0031.png?time=1737840592857&key=809c469a7e8109e4f644520037d77f37
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0032.png?time=1737840592857&key=8a1aa8d72f6e215421fd927ad5812a26
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0033.png?time=1737840592858&key=525862e5d867430b56788bece618ed68
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0034.png?time=1737840592858&key=86672728994e57f373ee5bdb92f425ae
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0035.png?time=1737840592858&key=dc2f8b51b990053b429728f7f2f18161
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0036.png?time=1737840592858&key=52b36d0f50ce77c7ca81d1ea632b2226
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0037.png?time=1737840592858&key=56b27a58db644b1bcb560018d30283f5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0038.png?time=1737840592858&key=675f2d77bf8099c9a072c42d1e06b995
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0039.png?time=1737840592858&key=05e2dd348c8f3c692d923f673ef19c9a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0040.png?time=1737840592858&key=87116fbdf8742448008ae358386bb9c3
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0041.png?time=1737840592858&key=a3853a4976a4a3e2df67d4bce8b809e8
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0042.png?time=1737840592858&key=b896393064cded388891006e8bfabb1b
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0043.png?time=1737840592858&key=47587958e9bd478a950b7efd2c416f1a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0044.png?time=1737840592858&key=56cc8fa4d5e4a9c8568b49ea343d6924
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0045.png?time=1737840592858&key=62af2bb4a8f4bcf7481a3ad61eebdb29
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0046.png?time=1737840592858&key=9d6e71f680c83bc64f21b73e17da16ab
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0047.png?time=1737840592858&key=b6f4c58bd063cb4ede19c7ed327b42d5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0048.png?time=1737840592858&key=7b5a403d698be364b9977a5d56822109
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0049.png?time=1737840592858&key=e495260ae8a2911249f4bffec54817cb
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0050.png?time=1737840592858&key=51c73a49c924cb37ace4574838a25eb5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0051.png?time=1737840592858&key=271d11e14ef5e3a448e03722c2c272bf
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0052.png?time=1737840592858&key=520f1f8eed55fc4e4e3493d100342491
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0053.png?time=1737840592858&key=977bc87db32433d9edc262ca852e0b11
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0054.png?time=1737840592858&key=7f689e2e974c26d3af9b35bc57086201
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0055.png?time=1737840592858&key=e0f17608e1c74c1f39dbc4af9cd2153a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0056.png?time=1737840592858&key=717097ebcf2f5d1d6529d9faf7ce7a72
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0057.png?time=1737840592858&key=28d387ccd02807ae3800a52f6d292630
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0058.png?time=1737840592858&key=ff9ac301bc74f2d8e6a3636bf3ddf556
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0059.png?time=1737840592858&key=3f64560edabc03c7d8d374f31956a071
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0060.png?time=1737840592858&key=12e3d47838540c1347bf2db25b3f4af5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0061.png?time=1737840592858&key=2b6463c01f14ac3dd879f0bcf40267c5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0062.png?time=1737840592858&key=cc0f90ca6a90e6b159c1ce141326a8f5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0063.png?time=1737840592858&key=378b8c731ea3ce68d4b670158925f7f0
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0064.png?time=1737840592859&key=d502af7ee9dcc78720da3f9b49d50978
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0065.png?time=1737840592859&key=b1f46a31dbac9339c5a9aff35342c2c5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0066.png?time=1737840592859&key=4fc293cf430db16e9b37fe65f1ce8dc9
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0067.png?time=1737840592859&key=aeac8862b81af40561536aa5ee24f143
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0068.png?time=1737840592859&key=2ea94739540e9522b9b1829a075b127e
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0069.png?time=1737840592859&key=cd39f59d4f4b94040bf3fa5180802fb7
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0070.png?time=1737840592859&key=cc1ee5942e7661ded848d8bf236fdc49
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0071.png?time=1737840592859&key=215c40c9d6635b4127348120df602ad5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0072.png?time=1737840592859&key=88502728596b0378c3e783b632204238
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0073.png?time=1737840592859&key=8011dee8b2814b5a07d65531af8e511b
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0074.png?time=1737840592859&key=0fea1b41d54576b57704d740f21d72c7
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0075.png?time=1737840592859&key=68f8ee96f0142ffaf4ec709eea69e202
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0076.png?time=1737840592859&key=237b4b9962c3e330f872d5321eab341f
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0077.png?time=1737840592859&key=f81cc0394637c2ae55a8e037161f1a54
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0078.png?time=1737840592859&key=cfde3f4078fddf67d87d15b23a98e806
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0079.png?time=1737840592859&key=f083c0fc8f02e35308700bec659260ca
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0080.png?time=1737840592859&key=8f4d3a51bdb9e87518a9b428c12db131
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0081.png?time=1737840592859&key=0efd443ba2afb6a72d5079038e157a19
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0082.png?time=1737840592859&key=eb42f7daf1208d2d5bd09ca049f94fb7
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0083.png?time=1737840592859&key=7e2b7263ee94d9b389ca34035093c56a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0084.png?time=1737840592859&key=a568286e00ae5fb2af2499c241063b95
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0085.png?time=1737840592859&key=47b376045f1498da96774adcd65a2ea6
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0086.png?time=1737840592859&key=cf5713ac267e17aebad662d78b648ade
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0087.png?time=1737840592859&key=f6b6a1fa33787cffb54f46ae9a0ed397
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0088.png?time=1737840592859&key=f9a1cce570acf7420b6aafd47c79f3d5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0089.png?time=1737840592859&key=130c5a072d6f5b93278a6b772a8adbdd
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0090.png?time=1737840592859&key=cd4a14d3fc04f1f6a425938f6ea18029
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0091.png?time=1737840592859&key=db5fc85eea21ea75d5f4c3eeafa285e8
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0092.png?time=1737840592859&key=6ac1522d4de4976015e862e13952528a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0093.png?time=1737840592859&key=bc7d669515ac88067a4bd98e90fcb4ed
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0094.png?time=1737840592859&key=b9402bc48da326c7d74c856e4eef7238
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0095.png?time=1737840592860&key=062b886736788f3a9644db7685d6db8e
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0096.png?time=1737840592860&key=ad308863c4a72e0118ef806be81e55c4
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0097.png?time=1737840592860&key=ff65f3b5cd02608aef2d36ff69a4963e
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0098.png?time=1737840592860&key=d6aa017827c660fcdaaa29253077958a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0099.png?time=1737840592860&key=91d45539f41a3755dfee5c1d36fae5a4
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0100.png?time=1737840592860&key=911c4d24cfd5583e9402521d67548862
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0101.png?time=1737840592860&key=66bd1de1f930e2d9c5b29138f50f995b
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0102.png?time=1737840592860&key=e3667806868081c952927b1c96620246
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0103.png?time=1737840592860&key=d31d1260dd5be02d57c03b4a684fcc41
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0104.png?time=1737840592860&key=14d407b31a453e1ef8da96404c2f8d20
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0105.png?time=1737840592860&key=51e584438bd93481ca2a174455d42216
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0106.png?time=1737840592860&key=abc904dd56d3d4c81a79c9d999ccdd2b
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0107.png?time=1737840592860&key=8a1b314a5e3052b9d7519d8deebce57f
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0108.png?time=1737840592860&key=c9aaa2c8642a514a3a33fac016d24ea0
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0109.png?time=1737840592860&key=bbf10da92c7708bc54c397cf6fcc72cc
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0110.png?time=1737840592860&key=5e26d9c76b34133f74a94abc304c086d
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0111.png?time=1737840592860&key=481cebe54ec8f176867fcf6533e321b8
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0112.png?time=1737840592860&key=b1fdd49ca5dedaae1fb679df6c077859
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0113.png?time=1737840592860&key=1bf4b5bc0dc38e2c25f15b9e58dac275
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0114.png?time=1737840592860&key=b3d2941d09a5c6ed5f8eb93b0e7b6fdf
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0115.png?time=1737840592860&key=3f81264a55f00cabe3014be1382d1117
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0116.png?time=1737840592860&key=9d0e4c68fb80f466df5896256cd0f734
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0117.png?time=1737840592860&key=3e59f75250fa408b7d64dc453989a1a2
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0118.png?time=1737840592860&key=2bf867fa63ad6c062d0915b1be91ccfe
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0119.png?time=1737840592860&key=df021d8ef23426d5d3fbdbc9679f8eca
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0120.png?time=1737840592860&key=fefe77c8d5f0bf451615639f78a215c8
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0121.png?time=1737840592860&key=1350b6c1f6159747ee2e79dcd6ca12d9
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0122.png?time=1737840592860&key=9168f94364d5a5357001f1eaa5e9fbf6
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0123.png?time=1737840592860&key=16d5eddbe31d22fc22331021c3a6e572
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0124.png?time=1737840592860&key=ab63c60461fe7dfaa761fd8be33b420f
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0125.png?time=1737840592860&key=637364a61cb367f8a0fabfc9e0bd2c8d
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0126.png?time=1737840592860&key=873222f76d1fed9e923dad0fae53b9a4
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0127.png?time=1737840592861&key=e9659febf59e5fd3ca1c166db6ccee1d
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0128.png?time=1737840592861&key=db8d70e06d9876d28c453da15af5466f
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0129.png?time=1737840592861&key=056b1150c201e44b4bb698707bb3c432
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0130.png?time=1737840592861&key=06e9156547742fcd14e00ea65f808319
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0131.png?time=1737840592861&key=d4beb78df749192485bb6a66b40cc87c
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0132.png?time=1737840592861&key=a3390819b193451e2baf821622ed2458
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0133.png?time=1737840592861&key=58e7f0d2a6dc2c597426a3e412231775
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0134.png?time=1737840592861&key=a0f5b0a709ca9d25b7609a50ea9e1bce
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0135.png?time=1737840592861&key=40b17b9400583da6b80fbb656994fd64
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0136.png?time=1737840592861&key=1048683bfb893c021ef56621080a2372
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0137.png?time=1737840592861&key=0d9299811f43680734adf2d22a07d856
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0138.png?time=1737840592861&key=0aedfe6b731cf254f651f5024ae6da87
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0139.png?time=1737840592861&key=0e4f659f94a9bf2f27ef4ea0371b1a84
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0140.png?time=1737840592861&key=06e4e47c8f7978636db40f84c80da0a8
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0141.png?time=1737840592861&key=b98ce89dc936e21c1a7c4b2f10df82e7
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0142.png?time=1737840592861&key=652eaee5922f3ac9764542006bdd3552
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0143.png?time=1737840592861&key=ea98e1701467b4809e75dd59531c1a8c
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0144.png?time=1737840592861&key=b955e9aabf8527611310c162e681c46b
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0145.png?time=1737840592861&key=a80ec61b990ce44ef5681b8629b4ae7d
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0146.png?time=1737840592861&key=e0c7a959b76916cdcc0242cfa574bde6
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0147.png?time=1737840592861&key=391bc46915503027950668b72b05cd36
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0148.png?time=1737840592861&key=6f2a5fc73ed4b9c79dc176b30fdce530
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0149.png?time=1737840592861&key=0f28b538221f5bcefce008db91433781
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0150.png?time=1737840592861&key=4b77a337127e7d40cc679f065be40888
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0151.png?time=1737840592861&key=ef666000d1fbee6ee0e280c03d3abdd2
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0152.png?time=1737840592861&key=05621cbb2e77139b64ae80960dd23dff
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0153.png?time=1737840592861&key=e9b5afaab1d45a19e42999de0fc56542
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0154.png?time=1737840592861&key=4ddeeedab038b2fa5329ddbd071c9bac
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0155.png?time=1737840592861&key=1e1829e4201d5cf1ff9198a9ffc56d98
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0156.png?time=1737840592861&key=52342e21c740dcfcb4e239e0fcc1af0b
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0157.png?time=1737840592861&key=f5cc29b01d1f9d1c8dee60d40b2d2bc5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0158.png?time=1737840592861&key=0c0fbbbd3e78b5b12ea5a4449989f4a5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0159.png?time=1737840592861&key=58a142b0ff5d6de9b988e3ee3598284f
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0160.png?time=1737840592862&key=c6f60d94c49b48a076abb9666ab2bbe6
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0161.png?time=1737840592862&key=749a174f2f40d9e9d0654f05ed75475a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0162.png?time=1737840592862&key=097ee8f41e0f04dae7d170a931532e0e
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0163.png?time=1737840592862&key=4b43c01d9e3de10c0b00e17a989b95e2
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0164.png?time=1737840592862&key=a212a9c783472687b2a0eaa367a5c722
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0165.png?time=1737840592862&key=9fe56a6976797ad585ed518ef19ad377
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0166.png?time=1737840592862&key=a61b1b665985c49cdade530a596c83de
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0167.png?time=1737840592862&key=a8db7648f97f05f940d7704e8c1ed146
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0168.png?time=1737840592862&key=0e2a8db16f8d676d6182c583a6c503aa
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0169.png?time=1737840592862&key=d7c851ed23e0201839fbfe3e5666082e
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0170.png?time=1737840592862&key=c7ce5575d823680863d72a8e08c3c9cf
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0171.png?time=1737840592862&key=5665e6dbb054d39703f694b8b3e6f774
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0172.png?time=1737840592862&key=93e8ded37933607dff019c88171210eb
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0173.png?time=1737840592862&key=8ed409f35f8b21f2bf6e04c92d49164d
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0174.png?time=1737840592862&key=21226d38979c9e916caa11ce7fe55330
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0175.png?time=1737840592862&key=186ec9ee170270e3419645da1386d9d8
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0176.png?time=1737840592862&key=a767027919b9bf22a064203773d63613
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0177.png?time=1737840592862&key=406250089e53a1f684f64e8e262773ab
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0178.png?time=1737840592862&key=d59d55689b8ed3c181d29f4d4c2a7cdf
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0179.png?time=1737840592862&key=4cf479e1d07e1edd31a104bdf5c52a92
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0180.png?time=1737840592862&key=8cad851203d482409c74a166ccc17758
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0181.png?time=1737840592862&key=6fca720b5003a5ab7b5397e8d9bcc600
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0182.png?time=1737840592862&key=1ae4e51d37c5b10ee9dec7b22f540bd5
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0183.png?time=1737840592862&key=0b9755e66227965687bbe21364f54441
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0184.png?time=1737840592862&key=e2bac09a565cd63f572996d346056910
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0185.png?time=1737840592862&key=b3613812e42899f829b770ee1030cf2f
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0186.png?time=1737840592862&key=b4b47fb2a09e95059c02ee82b1a391b2
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0187.png?time=1737840592862&key=c732f5f07f40b004bf70fe71abf3988a
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0188.png?time=1737840592862&key=33c9cfb5e293a703d6b8edd77154025c
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0189.png?time=1737840592862&key=d8b5f3ef5c1d7b8dcae590ba4334dab1
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0190.png?time=1737840592862&key=3bba1955c2df63c273803b928bdabb05
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0191.png?time=1737840592862&key=4b033b3e307dfce63ac620ce9f2dc902
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0192.png?time=1737840592863&key=86c3cce58deac14771032b84b23a17b3
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0193.png?time=1737840592863&key=fbb5e5a38d7a2af6c272397624f0a014
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0194.png?time=1737840592863&key=26d772daa98106b8431d2ae7fe9d8abc
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0195.png?time=1737840592863&key=960795300eb410aa8a11049db7e50b87
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0196.png?time=1737840592863&key=92ba769b4348094cb78e899596b0396e
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0197.png?time=1737840592863&key=44d982d2b4be8db30a9abf1b0a3db58c
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0198.png?time=1737840592863&key=70cd4b87b36586c6cc403faa5cd508ac
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0199.png?time=1737840592863&key=006ead1b7284a6f79aa94c2ffba9d8ad
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0200.png?time=1737840592863&key=174e5715b4c9b0a01de45b92f46759d9
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0201.png?time=1737840592863&key=c6114b9ec4b243c0efdb4299cc430833
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0202.png?time=1737840592863&key=6133adeec18f33ae8f18fe1146c040ff
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0203.png?time=1737840592863&key=d001197a49d9fe37e165fc2a645111f2
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0204.png?time=1737840592863&key=69e8a2498e3a8cd8adf72b47f22e4c71
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0205.png?time=1737840592863&key=0e55a9505d1a580e774b05796faf78b3
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0206.png?time=1737840592863&key=bb91de4b19dcc4f5c2b14673cfbd5062
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0207.png?time=1737840592863&key=c011e3e0eb9f158e101083032a431ae6
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0208.png?time=1737840592863&key=956ed9dd895ed947128ffe988be4dc9c
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0209.png?time=1737840592863&key=3e4c5a58a8677dc050550c02d9419e18
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0210.png?time=1737840592863&key=d56f9b5cc0790a98a3830cc0bcc330c1
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0211.png?time=1737840592863&key=387d6ca89087b6ebad61af0706195151
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0212.png?time=1737840592863&key=6389da48decc51dda2ba9b06291fb1b8
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0213.png?time=1737840592863&key=260ca26ce5c8f6d0c236b44bf0470905
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0214.png?time=1737840592863&key=58a25f4a2156fe62c320a9f01b772f13
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0215.png?time=1737840592863&key=0cab931f3a979e736fe428b9a4e51894
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0216.png?time=1737840592863&key=a092d731e745e725885906865bd9be74
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0217.png?time=1737840592863&key=5e529080dd887e75f7847a4c69066113
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0218.png?time=1737840592863&key=7d6a09a76d609ac1a751461c1a0b1117
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0219.png?time=1737840592863&key=3ebb31ab4e8ef132027780642220a3ba
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0220.png?time=1737840592863&key=3153ac0bd13e5427c42f6e74cb96f438
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0221.png?time=1737840592863&key=f118238df2448c37bc03822b8e56b760
https://kazneb.kz/FileStore/dataFiles/f4/8e/1554745/content/0222.png?time=1737840592863&key=50317474ad20c7d21b4c27db4bf8bb90


'''

# Преобразуем многострочную строку в список URL--------------------------------------------------------
image_urls = image_urls.strip().splitlines()

# Папка для сохранения изображений
folder = r'C:\Users\asqaq\Desktop\kazneb\jukteu'

# Если папки нет, создаем ее
if not os.path.exists(folder):
    os.makedirs(folder)

# Создаем PDF для всех страниц
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Скачиваем и добавляем изображения в PDF
for idx, img_url in enumerate(image_urls):
    try:
        # Загружаем изображение
        img_data = requests.get(img_url).content
        img = Image.open(BytesIO(img_data))
        
        # Сохраняем изображение в папку
        img_path = os.path.join(folder, f'page_{idx + 1}.png')
        img.save(img_path)

        # Добавляем изображение в PDF
        pdf.add_page()
        pdf.image(img_path, x=10, y=10, w=180)  # Размеры и позиция могут быть изменены

        print(f"Страница {idx + 1} успешно сохранена в {img_path}.")
    except requests.exceptions.RequestException as e:
        print(f"Не удалось скачать страницу {idx + 1}: {e}")

# Сохраняем PDF
pdf_output = os.path.join(folder, 'document.pdf')
pdf.output(pdf_output)

print(f"PDF успешно сохранен в {pdf_output}.")
