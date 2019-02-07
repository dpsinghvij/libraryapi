from flask import Flask

app= Flask("libraryapp")

@app.route('/')
def index():
    return "Welcome to the Library"

if __name__ == '__main__':
    app.run()