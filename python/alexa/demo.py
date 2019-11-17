import alexandra

app = alexandra.Application()
name_map = {}

@app.launch
def launch_handler(*args):
    print("Args: {}".format(str(args)))
    return alexandra.respond("Hello, I'm a raspberry pi velcroed onto your freezer.")

if __name__ == '__main__':
    app.run('0.0.0.0', 8050, debug=True)

