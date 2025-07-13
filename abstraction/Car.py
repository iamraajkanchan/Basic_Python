class Car :
    def __init__(self, name):
        self.name = name
        self.useClutch = False
        self.useBreak = False
        self.useAccelerator = False

    def start(self):
        self.useBreak = False
        self.useClutch = True
        self.useAccelerator = True
        return f"Starting {self.name} when break applied: {self.useBreak}, clutch applied: {self.useClutch}, accelerator applied: {self.useAccelerator}"

    def stop(self):
        self.useBreak = True
        self.useClutch = True
        self.useAccelerator = False
        return f"Starting {self.name} when break applied: {self.useBreak}, clutch applied: {self.useClutch}, accelerator applied: {self.useAccelerator}"