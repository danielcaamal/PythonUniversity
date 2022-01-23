import logging as log


log.basicConfig(
    level=log.ERROR,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        log.FileHandler('data_layer.log'),
        log.StreamHandler()
    ]
)