import os
import argparse

import numpy as np
import pandas as pd
import pydicom
import scipy.misc
import scipy
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import cv2

from utils.parser import str2bool, str2time
from utils.logger import logger, init_logger
from utils.preprocess_helper import crop_center, segment, binarize
from data import load_images


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data',
                        type=str,
                        default='data/train',
                        const='data/train',
                        nargs='?',
                        choices=['data/train', 'data/test'],
                        help='choose between ["train", "test"]')
    parser.add_argument('--original', type=str, default='CT(CE)/2.PG+30/', help="original data path")
    parser.add_argument('--contrast', type=str, default='CT(CE)/2.PG+30/', help="contrast data path")
    parser.add_argument('--manufacturer',
                        type=str.lower,
                        default='all',
                        const='all',
                        nargs='?',
                        choices=['ge', 'siemens', 'all'],
                        help='choose between ["ge", "siemens", "all"]')
    parser.add_argument('--segmentation', type=str2bool, default='0',
                        help="do you need segmentation?")
    parser.add_argument('--crop', type=str2bool, default='0',
                        help="do you need crop?")
    parser.add_argument('--augmentation', type=str2bool, default='0', help="do you need augmentation?")
    parser.add_argument('--log-file', type=str, default='./logs/test.log', help="where do you want to log")
    args = parser.parse_args()
    return args


def preprocess_original(args, images):
    preprocessed_images = []

    for image in images:
        if args.crop:
            image = crop_center(image)
        if args.segment:
            image = segment(image)
        preprocessed_images.append(image)
    return preprocessed_images


def preprocess_contrast(args, images):
    preprocessed_images = []

    for image in images:
        if args.crop:
            image = crop_center(image)
        if args.segment:
            image = segment(image)
        if args.binarize:
            image = binarize(image)
        preprocessed_images.append(image)
    return preprocessed_images


def augment_original(args, images):
    pass


def augment_contrast(args, images):
    pass


def main():
    args = parse_args()
    init_logger(args)

    # load
    logger.info("LOAD IMAGE")
    original_images, contrast_images = load_images(args, logger)

    # preprocess
    logger.info("PREPROCESS")
    preprocessed_original = preprocess_original(args, original_images)
    preprocessed_contrast = preprocess_contrast(args, contrast_images)

    # augmentation
    logger.info("AUGMENT")
    augmented_original = augment_original(args, preprocessed_original)
    augmented_contrast = augment_contrast(args, preprocessed_contrast)

    #


if __name__ == "__main__":
    main()