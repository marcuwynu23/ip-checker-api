from flask import Flask, json, request
from app.ipchecker import get_ip_info, ping, check_service


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.routes()

    def routes(self):
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/api/checker", "ip", self.check)

    def index(self):
        return "Hello, World!"

    def check(self):
        hostname = request.args.get("hostname")
        ip_info = get_ip_info(hostname)
        ping_result = ping(hostname)
        common_service_ports = [80, 443, 22]
        service_info = {}
        for port in common_service_ports:
            service_info[port] = check_service(hostname, port)
        output_result = {
            "IP Info": ip_info,
            "Ping Result": ping_result,
            "Service Info": service_info
        }
        return output_result

    def run(self, debug=False, host="127.0.0.1", port=5000):
        self.app.run(debug=debug, host=host, port=port)
