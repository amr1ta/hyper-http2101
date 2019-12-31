import ssl
import hyper
from hyper.tls import init_context

# Custom SSLCONTEXT for not verifying SSLCertificate and Hostname
ssl_context = init_context()
hyper.tls._context = ssl_context
hyper.tls._context.check_hostname = False
hyper.tls._context.verify_mode = ssl.CERT_NONE

conn = hyper.HTTP20Connection('localhost', port=7100, secure=True, ssl_context=ssl_context)
conn.request('GET', '/')

print(conn.get_response())