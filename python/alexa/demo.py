import alexandra

app = alexandra.Application()
name_map = {}

@app.launch
def launch_handler(session):
    print("Session: {}".format(str(session)))
    return alexandra.respond("Hello, I'm a raspberry pi velcroed onto your freezer.")

if __name__ == '__main__':
    app.run('0.0.0.0', 8050, debug=True)

