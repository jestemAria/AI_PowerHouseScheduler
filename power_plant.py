class PowerPlant:

    to_become_active = 0

    def __init__(self, unit_id, unit_capacity, unit_maintenance_period):
        self.unit_id = unit_id
        self.unit_capacity = unit_capacity
        self.unit_maintenance_period = unit_maintenance_period
        self.active = True

    def activate(self):
        self.active = True

    def deactivate(self, unit_maintenance_period):
        self.active = False
        global to_become_active
        self.to_become_active = unit_maintenance_period

    def repair(self):
        to_become_active -= 1
        if to_become_active == 0:
            PowerPlant.activate(self)
