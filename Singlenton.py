import threading

class SinglentonClass(object):

    _instance_lock = threading.Lock()

    def __init__(self):

        pass


    def __new__(cls, *args, **kwargs):
        cls.mywebdriver = None

        if not hasattr(SinglentonClass, "_instance"):
            with SinglentonClass._instance_lock:
                if not hasattr(SinglentonClass, "_instance"):
                    SinglentonClass._instance = object.__new__(cls)

        return SinglentonClass._instance

    def task(arg):
        obj = SinglentonClass()
        print(obj)



