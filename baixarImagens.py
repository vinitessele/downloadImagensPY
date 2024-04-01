from bing_image_downloader import downloader #pip install bing_image_downloader

filtro = 'maçã'
destino = 'D:\\ImagensDigitaisPy\\Treinamento Yolo\\img\\dataset'

print('Iniciando downloads...')
try:
    downloader.download(filtro, limit=1, output_dir=destino, adult_filter_off=True)

    print('Download concluído!')
except Exception as e:
    print("Ocorreu um erro:", e)