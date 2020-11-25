def debug(fn):
    def inner(*args):
        try:
            fn(*args)
        except Exception as e:
            print("Error while calling:", fn.__name__, "\nException:", e)
    return inner