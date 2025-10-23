from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

# Usuarios de prueba
USERS = {
    'admin': 'admin123',
    'user': 'password',
    'demo': 'demo123'
}

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('login.html', 'rb') as f:
                self.wfile.write(f.read())
        
        elif self.path == '/styles.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('styles.css', 'rb') as f:
                self.wfile.write(f.read())
        
        elif self.path == '/script.js':
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            with open('script.js', 'rb') as f:
                self.wfile.write(f.read())
        
        elif self.path == '/dashboard':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Dashboard</title>
                <link rel="stylesheet" href="styles.css">
            </head>
            <body>
                <div class="container">
                    <div class="login-box">
                        <h1>¡Bienvenido al Dashboard!</h1>
                        <p class="subtitle">Has iniciado sesión correctamente</p>
                        <button onclick="window.location.href='/'" class="btn-login">Cerrar Sesión</button>
                    </div>
                </div>
            </body>
            </html>
            '''
            self.wfile.write(html.encode())
        
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            username = data.get('username', '')
            password = data.get('password', '')
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if username in USERS and USERS[username] == password:
                response = {
                    'success': True,
                    'username': username,
                    'message': 'Login exitoso'
                }
            else:
                response = {
                    'success': False,
                    'message': 'Usuario o contraseña incorrectos'
                }
            
            self.wfile.write(json.dumps(response).encode())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, LoginHandler)
    print(f'Servidor corriendo en http://localhost:{port}')
    print(f'Usuarios de prueba:')
    for user, pwd in USERS.items():
        print(f'  - Usuario: {user} | Contraseña: {pwd}')
    print('\nPresiona Ctrl+C para detener el servidor')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
