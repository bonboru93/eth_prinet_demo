import time
from briReader import BriReader
from ethPoster import EthPoster

br = BriReader()
br.start()

ep = EthPoster()

second = 0

while True:
        print(br.value)
        if (second == 15):
                ep.post(br.value)
                second = 0
        time.sleep(1)
        second += 1