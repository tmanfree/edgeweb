#!/usr/bin/env python3

from EdgeWeb.application import app

def edgeweb():
    print("HELLO")
    print("test")

if __name__ == "__main__":
    edgeweb()
    app.run(debug=False)