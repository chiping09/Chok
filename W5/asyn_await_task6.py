import asyncio
import time

async def ioioio(wela, chue_ngan):
    print('เริ่ม %s เวลาผ่านไปแล้ว %.6f วินาที' % (chue_ngan, time.time() - t0))
    await asyncio.sleep(wela)
    print('%s เสร็จแล้ว เวลาผ่านไปแล้ว %.6f วินาที' % (chue_ngan, time.time() - t0))

async def main():
    cococoru = [
        ioioio(1.5, 'โหลดเพลง'),
        ioioio(2.5, 'โหลดอนิเมาะ'),
        ioioio(0.5, 'โหลดหนัง'),
        ioioio(2, 'โหลดเกม')
    ]
    await asyncio.gather(*cococoru)

t0 = time.time()
asyncio.run(main())
