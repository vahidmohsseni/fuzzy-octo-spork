import os

import Server

app = Server.create_app()


if __name__ == '__main__':

    PORT = int(os.environ.get('PORT', 5000))
    print("logs available")
    app.run(host='0.0.0.0', port=PORT, debug=True)
