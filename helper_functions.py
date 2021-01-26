from requests import get

def get_my_ip():
    ip = get('https://api.ipify.org').text
    ip_address = 'IP ADDRESS : PORT ===> {}'.format(ip)
    return ip_address
if __name__ == "__main__" :
    get_my_ip()