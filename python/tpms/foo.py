import traceback

try:
    print(5/0)
except Exception as e:
    print(traceback.format_exception(e))

