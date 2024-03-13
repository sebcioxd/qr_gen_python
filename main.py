import segno
import os, shutil
from pathlib import Path


def get_input():
    input_url = input("Please provide a link, or any text you want to convert into your qr code! ")
    return input_url


def get_title():
    title = input("Please provide your qr code title! ")
    return title


def get_qr(url, title):
    qrcode = segno.make_qr(str(url))
    qrcode.save(
        f"{title}.png",
        scale=10,
        border=1,
    )


def main():
    title = get_title()
    url = get_input()
    path = str(os.path.join(Path.home(), 'Downloads'))

    get_qr(url, title)
    try:
        shutil.move(f"{title}.png", path)
    except:
        print("Hey, there is a issue because the name of your qr code already exists in downloads! please remove it or try with different name...")
        input("Press enter to exit... ")
        exit()
    print(f"The file has been stored in your Downloads as {title}.png!")


if __name__ == '__main__':
    main()
    input("Press enter to exit... ")