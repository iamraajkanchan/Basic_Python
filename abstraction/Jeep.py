from .Vehicle import Vehicle

class Jeep(Vehicle) :
    # If you don't override all the abstract methods of Vehicle class, you will face a runtime error.
    # You won't face a compile time error.

    def start_engine(self):
        print("Starting Jeep")
        pass

    def stop_engine(self):
        print("Stopping Jeep")
        pass

    def get_fuel_type(self):
        pass
        return "Diesel"






