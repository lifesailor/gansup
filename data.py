import os
import pydicom


def load_images(args, logger):

    base_path = os.path.abspath(args.data)
    original_path = args.original
    contrast_path = args.contrast

    files = os.listdir(base_path)
    files.sort()
    files = [file for file in files if '_' not in file and ' ' not in file]
    original_total_path = [os.path.join(os.path.join(base_path, file), original_path) for file in files]
    contrast_total_path = [os.path.join(os.path.join(base_path, file), contrast_path) for file in files]

    logger.info("LOAD DICOM FILES")
    original_total_files = load_files(original_total_path)
    contrast_total_files = load_files(contrast_total_path)

    logger.info("SELECT FILE BY MANUFACTURER")
    original_files = get_manufacturer_files(args.manufacturer, original_total_files)
    contrast_files = get_manufacturer_files(args.manufacturer, contrast_total_files)
    logger.info("GE: %d " % len(original_files))
    logger.info("SIEMNES: %d " % len(contrast_files))

    logger.info("GET IMAGES")
    original_images = get_images(original_files)
    contrast_images = get_images(contrast_files)
    return original_images, contrast_images


def load_files(path):
    total_files = []

    # folder
    for base_path in path:
        files = os.listdir(base_path)
        files.sort()

        # files
        folder_files = []
        for file in files:
            data = pydicom.dcmread(os.path.join(base_path, file))
            folder_files.append(data)
        total_files.append(folder_files)
    return total_files


def get_images(files):
    total_images = []

    # folder
    for file in files:
        sequence_image = []

        # files
        for sequence in file:
            sequence_image.append(sequence.pixel_array)
        total_images.append(sequence_image)
    return total_images


def get_manufacturer_files(manufacturer, files):
    manufacturer_files = []

    if manufacturer == 'all':
        return files
    else:
        for file in files:
            if manufacturer == check_manufacturer(file):
                manufacturer_files.append(file)
        return manufacturer_files


def check_manufacturer(file):
    file_info = file[0]
    file_info = str(file_info)
    manufacturer = file_info.split('Manufacturer')[1]
    manufacturer = manufacturer.split('\n')[0].split('LO:')[1].lower()

    if 'ge' in manufacturer:
        return 'ge'
    else:
        return 'siemens'
