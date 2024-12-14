import json
def cmd(*arguments):
    _ = list(arguments)
    del(_[0])
    del(_[0])
    command = " ".join(_)
    try:
        a = str(eval(command))
    except Exception as e:
        a = e
    return a