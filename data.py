import os
import pydicom


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


def load_images(files):
    total_images = []

    # folder
    for file in files:
        sequence_image = []

        # files
        for sequence in file:
            sequence_image.append(sequence.pixel_array)
        total_images.append(sequence_image)
    return total_images