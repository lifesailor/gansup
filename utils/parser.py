import argparse
from time import gmtime, strftime


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def str2time():
    return strftime("%Y-%m-%d %H:%M:%S.log", gmtime())
