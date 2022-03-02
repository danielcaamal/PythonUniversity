'''HOW TO LOGGING:
    - DEBUG: Detailed information, typically of interest only when diagnosing problems.
    - INFO: Confirmation that things are working as expected.
    - WARNING: And indication that something unexpected happened, or indicative of some problem near future. 
        The software is still working as expected.
    - ERROR: Due to a more serious problem, the software has not been able to perform some function.
    - CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
'''

import logging as log


log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        log.FileHandler('data_layer.log'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('DEBUG message')

    log.info('INFO message')

    log.warning('WARNING message')

    log.error('ERROR message')

    log.critical('CRITICAL message')