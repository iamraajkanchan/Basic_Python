from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        """Start the vehicle's engine."""
        pass

    @abstractmethod
    def stop_engine(self):
        """Stop the vehicle's engine."""
        pass

    @abstractmethod
    def get_fuel_type(self):
        """Return the type of fuel used."""
        pass

    def honk(self):
        """Make a honking sound"""
        return "Beep Beep!"
