from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy import ctx
import os

class SSLProxy:
    def __init__(self):
        self.config = proxy.ProxyConfig(options.Options())

    def request(self, flow):
        
        pass

    def response(self, flow):
        
        pass

    def error(self, flow):
        
        pass

    def run(self):
        # mitmproxy options
        opts = options.Options()
        opts.add_option("ssl_insecure", bool, True, "")
        opts.add_option("ssl_verify_upstream_cert", bool, False, "")

        # Configure mitmproxy master
        master = DumpMaster(opts)
        master.server = proxy.ProxyServer(self.config)

        
        master.addons.add(self)

        
        try:
            master.run()
        except KeyboardInterrupt:
            master.shutdown()

if __name__ == "__main__":
    #Configure SSL certificate
    os.system("mitmproxy -s \"mitmdump -p 8080 -w output_file\" --listen-host 0.0.0.0 --listen-port 8080 --mode transparent")

    # Start the server
    ssl_proxy = SSLProxy()
    ssl_proxy.run()
