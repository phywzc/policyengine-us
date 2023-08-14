from policyengine_us.model_api import *


class InnovativeMotorVehicleOwnership(Enum):
    VECHICLE_PURCHASE = "Vehicle Purchase"
    VECHICLE_LEASE = "Vehicle Lease"
    OTHER = "Other"


class innovative_motor_vehicle_ownership(Variable):
    value_type = Enum
    possible_values = InnovativeMotorVehicleOwnership
    default_value = (
        InnovativeMotorVehicleOwnership.OTHER
    )  # OTHER is not included in the form, I consider OTHER as invalid for the credit.
    entity = TaxUnit
    label = "Colorado innovative motor vechicle ownership "
    definition_period = YEAR
