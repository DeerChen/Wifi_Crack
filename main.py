'''
Description: 无线爆破
Author: Senkita
Date: 2021-02-13 21:29:30
LastEditors: Senkita
LastEditTime: 2021-02-15 09:08:43
'''
import os
import sys
from wifi_crack.utils import WifiCrack


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)


def main() -> None:
    wifi_crack = WifiCrack.WifiCrack()
    wifi_crack.check_password()


if __name__ == '__main__':
    main()
