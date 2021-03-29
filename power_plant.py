class powerplant:

    def _init_(self, code, generatedPower, maintainancePeriod, active):
        self.code = code
        self.generatedPower = generatedPower
        self.maintainancePeriod = maintainancePeriod
        self.active = active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

