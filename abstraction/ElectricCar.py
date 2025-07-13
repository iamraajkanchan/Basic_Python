from .Vehicle import Vehicle


class ElectricCar(Vehicle):

    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity
        self.motor_running = False

    def start_engine(self):
        self.motor_running = True
        return f"{self.brand} {self.model} electric motor started silently"

    def stop_engine(self):
        self.motor_running = False
        return f"{self.brand} {self.model} electric motor stopped"

    def get_fuel_type(self):
        return "Electricity"

    def get_battery_info(self):
        return f"Battery Capacity : {self.battery_capacity} kwh"
