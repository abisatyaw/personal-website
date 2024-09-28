import waitress

from app import app

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = '8080'
    print(f"INFO!! waitress:Serving on http://{HOST}:{PORT}")
    waitress.serve(app, host=HOST, port = PORT,  url_scheme='https', expose_tracebacks=True)