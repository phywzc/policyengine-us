from policyengine_us.model_api import *


class gross_vehicle_weight_rating(Variable):
    value_type = float
    entity = TaxUnit
    label = "Gross vehicle weight rating of target vehicle (Colorado innovative truck)"
    documentation = "The Gross Vehicle Weight Rating (GVWR) is a metric that represents the maximum weight that a vehicle is safely rated to carry."
    unit = "/1"
    definition_period = YEAR
