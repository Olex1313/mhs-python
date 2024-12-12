import asyncio
import os
import aiohttp
import sys


async def download_random_file(coro_num: int, folder: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://picsum.photos/200/300", allow_redirects=True
        ) as response:
            if response.status == 200:
                with open(f"{folder}/picture-{coro_num}.jpg", "wb") as fd:
                    async for chunk in response.content.iter_chunked(1024 * 1024):
                        fd.write(chunk)


async def main():
    if len(sys.argv) < 2:
        raise RuntimeError("USAGE: python downloader.py [folder] [images_amount]")
    amount = int(sys.argv[1])
    download_folder = sys.argv[2]

    if not os.path.isdir(download_folder):
        raise RuntimeError(f"dir {download_folder} does not exist")

    async with asyncio.TaskGroup() as tg:
        for i in range(amount):
            tg.create_task(download_random_file(i, download_folder))


if __name__ == "__main__":
    asyncio.run(main())
