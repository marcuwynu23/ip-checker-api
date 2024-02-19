
import socket
import subprocess
import platform


def get_ip_info(hostname):
    ip_info = {}
    try:
        ip = socket.gethostbyname(hostname)
        ip_info["IP Address"] = ip
        ip_info["Hostname"] = socket.gethostbyaddr(ip)[0]
        ip_info["OS"] = platform.system()
        ip_info["OS Version"] = platform.release()
    except socket.error:
        ip_info["Error"] = "Unable to resolve hostname."
    return ip_info


def ping(host):
    ping_result = {}
    try:
        subprocess.check_call(["ping", "-c", "1", host])
        ping_result["Ping"] = "Successful"
    except subprocess.CalledProcessError:
        ping_result["Ping"] = "Unsuccessful"
    return ping_result


def check_service(host, port):
    service_info = {}
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        if result == 0:
            service_info["Service"] = f"Running on port {port}"
        else:
            service_info["Service"] = f"Not running on port {port}"
        sock.close()
    except socket.error:
        service_info["Error"] = "Error checking service."
    return service_info
