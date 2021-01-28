from requests import get
import ctypes


def get_my_ip():
    ip = get('https://api.ipify.org').text
    ip_address = 'IP ADDRESS : PORT ===> {}'.format(ip)
    return ip_address


def screen_resolution():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    if screensize == (1366, 768):
        size = 'Your screen resolution is OK: {}'.format(screensize)
    else:
        size = 'WRONG SCREEN RESOLUTION: {} \n SET YOUR SCREEN RESOLUTION TO (1366, 768) AND RESTART THE SERVER!!!!'.format(screensize)
    return size


if __name__ == "__main__":
    get_my_ip()
