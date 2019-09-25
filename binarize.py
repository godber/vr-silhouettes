#!/usr/bin/env python

from pathlib import Path

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def convert_and_save(img, name):
    '''Converts from Numpy Array to PIL Image then saves'''
    Image.fromarray(img).save(name)


def binarize(img):
    '''Blurs image then does thresholding on that image array, returns image array'''
    blur = cv2.GaussianBlur(img, (5,5), 0)
    _, img_thold = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    # return Image.fromarray(img_thold)
    return img_thold


def find_largest_blob(img):
    '''Dilates image array, finds largest area contour returns blob from that area'''
    kernel = np.ones((25,25), np.uint8) 
    img_dilated = cv2.dilate(img, kernel, iterations=1)

    convert_and_save(img_dilated, 'dilated.png')

    # Get Contours of dilate image
    _, contours, _ = cv2.findContours(img_dilated, 1, 2)

    if len(contours) > 0:
        # find the index of the largest contour by area
        largest_contour_index, _ = max(enumerate(
            map(cv2.contourArea, contours)),
            key=lambda item: item[1]
        )

    mask = np.zeros_like(img)
    out = np.zeros_like(img)

    # Draw filled contour in mask
    cv2.drawContours(mask, contours, largest_contour_index, 255, -1)
    # Extract out the object and place into output image
    out[mask == 255] = img[mask == 255]
    return out


def insert_suffix(image_file, suffix):
    p = Path(image_file)
    outdir = Path.joinpath(p.parent, suffix)
    Path.mkdir(outdir, exist_ok=True)
    return Path.joinpath(outdir, p.stem + '_'+ suffix + p.suffix)


def mask_logo(img):
    img[370:422, 498:573] = 0
    return img


def main(image_file):
    print(f'processing: {image_file}.')
    img = cv2.imread(image_file, 0)

    img_binarized = binarize(img)
    convert_and_save(img_binarized, insert_suffix(image_file, 'binarized'))

    img_bin_and_masked = mask_logo(img_binarized)
    convert_and_save(img_bin_and_masked, insert_suffix(image_file, 'masked'))

    largest_blob = find_largest_blob(img_binarized)
    convert_and_save(largest_blob, insert_suffix(image_file, 'blob'))


# binarize.py /srv/godber/temp/xxoutput_4981.jpg
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(args.file)
