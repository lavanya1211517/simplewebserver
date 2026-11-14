from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>laptop Device Information</title>
    </head>
    <body>
        <h1>Lavanya V (26009527)</h1>

        <table border="1" cellspacing="10" cellpaddiing="10">
          <tr bgcolor="">
            <th>S.no</th>
            <th>Device Name</th>
            <th>Installed Ram</th>
            <th>Processor</th>
            <th>System Type</th>
            <th>storage</th>
            <th>Device ID</th>
            <th>Product ID</th>
          </tr>
          <tr>
            <td>1</td>
            <td>TL15-53M-G2</td>
            <td>16.0 GB(15.7 GB usable) </td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
            <td>64-bit operating system, x64-based processor</td>
            <td>130 GB of 477 GB used</td>
            <td>71A6EEFB-94A1-4093-92E5-CA3C04EEA372</td>
            <td>00342-42943-38785-AAOEM</td>
          </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()