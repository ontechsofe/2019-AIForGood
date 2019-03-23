from flask import Flask

if __name__ == "__main__":
    app = create_app("config")
    app.run(port=5001, debug=True)