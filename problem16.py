import os
import time
import sys
import aiohttp
import asyncio


POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://52.14.205.215/flags/'

DEST_DIR = 'downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


async def get_flag(cc_list):
    async with aiohttp.ClientSession() as session:
        for cc in cc_list:
            url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
            async with session.post(url=url) as resp:
                image = await resp.read()
                show(cc)
                save_flag(image, cc.lower() + '.gif')

def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def main():
    t0 = time.time()
    loop = asyncio.get_event_loop()
    sorted_flag_list = sorted(POP20_CC)
    loop.run_until_complete(get_flag(sorted_flag_list))
    count = len(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main()









