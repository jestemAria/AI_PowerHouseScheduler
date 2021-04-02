class PowerPlant:

    def __init__(self, unit_id, unit_capacity, unit_maintenance_period):
        self.unit_id = unit_id
        self.unit_capacity = unit_capacity
        self.unit_maintenance_period = unit_maintenance_period
        self.active = True

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

