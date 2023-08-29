from policyengine_us.model_api import *


class InnovativeTruckFuelType(Enum):
    ELECTRIC_TRUCK = "Electric Truck"
    PLUG_IN_HYBRID_ELECTRIC_TRUCK = "Plug-in Hybrid Electric Truck"
    OTHER = "Other"


class innovative_truck_fuel_type(Variable):
    value_type = Enum
    possible_values = InnovativeTruckFuelType
    default_value = InnovativeTruckFuelType.OTHER
    entity = TaxUnit
    label = "Colorado innovative truck fuel type "
    definition_period = YEAR
