class Logger(object):
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            print("Creating the user number")
            cls.__instance = super(Logger,cls).__new__(cls)
            return cls.__instance


Log1 = Logger()
print(Log1)

Log2 = Logger()
print(Log2)
#Did not print becuase only one can be created