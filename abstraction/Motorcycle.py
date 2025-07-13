from .Vehicle import Vehicle


class MotorCycle(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_running = False

    def start_engine(self):
        self.engine_running = True
        return f"{self.brand} {self.model} motor cycle engine started running"

    def stop_engine(self):
        self.engine_running = False
        return f"{self.brand} {self.model} motor cycle engine stopped running"

    def get_fuel_type(self):
        return "Gasoline"
