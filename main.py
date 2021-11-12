# -*- coding: utf-8 -*-
import pyautogui
from PIL import Image
import re
import glob, os
import img2pdf
from natsort import natsorted #自然順にするため

def next_page():
  pyautogui.click(938, 568)

def take_screen_shot(number):
  sc = pyautogui.screenshot(region=(80, 65, 860, 1055))
  sc.save('image/page{}.png'.format(number))

def convert_to_jpeg():
  files = glob.glob("image/*.png")

  match = re.compile("(png)")

  for file_name in files:
      im = Image.open(file_name)
      im = im.convert("RGB")

      new_file_name = match.sub("jpeg", file_name)
      os.remove(file_name)
      im.save(new_file_name, quality=100)

      print(file_name + " convert is completed")

def convert_to_pdf():
  pdf_file_name = "output.pdf"
  lists = list(glob.glob("./image/*.jpeg"))
  with open(pdf_file_name, "wb") as f:
    f.write(img2pdf.convert([str(i) for i in natsorted(lists) if ".jpeg" in i]))

if __name__ == '__main__':
  pages = 5
  os.makedirs('./image', exist_ok=True)
  for i in range(pages):
    take_screen_shot(i)
    next_page()
  convert_to_jpeg()
  convert_to_pdf()