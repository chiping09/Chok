import asyncio
import time

async def ioioio(wela, chue_khanom):
    print('เริ่มอบ %s เวลาผ่านไปแล้ว %.6f วินาที' % (chue_khanom, time.time() - t0))
    await asyncio.sleep(wela)
    print('อบ%s เสร็จแล้ว เวลาผ่านไปแล้ว %.6f วินาที' % (chue_khanom, time.time() - t0))
    return '*'+chue_khanom+'อบเสร็จ'

async def main():
    cococoru = [
        ioioio(1.5, 'เต้าหู้'),
        ioioio(2.5, 'เค้ก'),
        ioioio(0.5, 'ไส้กรอก'),
        ioioio(2, 'ครัวซอง')
    ]
    phonlap = await asyncio.gather(*cococoru)
    print(phonlap)

t0 = time.time()
asyncio.run(main())
