from policyengine_us.model_api import *


class innovative_motor_vehicle_passengers_seating(Variable):
    value_type = int
    entity = TaxUnit
    label = "Count of passenger seats in the innovative motor vehicle"
    unit = USD
    definition_period = YEAR
    reference="https://tax.colorado.gov/sites/tax/files/documents/DR_0617_2022.pdf#page=1"


