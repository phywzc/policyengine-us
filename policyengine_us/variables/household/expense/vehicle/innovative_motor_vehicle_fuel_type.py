from policyengine_us.model_api import *


class InnovativeMotorVehicleFuelType(Enum):
    ELECTRIC_VECHICLE = "Electric Vehicle"
    PLUG_IN_HYBRID_ELECTRIC_VECHICLE = "Plug-in Hybrid Electric Vehicle"
    OTHER = "Other"


class innovative_motor_vehicle_fuel_type(Variable):
    value_type = Enum
    possible_values = InnovativeMotorVehicleFuelType
    default_value = InnovativeMotorVehicleFuelType.OTHER
    entity = TaxUnit
    label = "Colorado innovative motor vechicle fuel type "
    definition_period = YEAR
