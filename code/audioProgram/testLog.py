
import sys
sys.path.append(r'../auxClass/')
from wangLog import WangLog

log2 = WangLog()

if __name__ == "__main__":

    for i in range(0, 10):
        log2.info('test')

        log2.error('test')

        log2.debug('test')
        log2.warn('test2')