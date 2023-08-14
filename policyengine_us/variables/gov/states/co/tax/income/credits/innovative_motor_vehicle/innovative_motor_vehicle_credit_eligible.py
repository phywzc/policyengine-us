from policyengine_us.model_api import *


class innovative_motor_vechicle_credit_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    definition_period = YEAR
    label = "Eligible for Colorado innovative motor vechicle credit"
    documentation = "Eligibility for Credit of Purchase or Lease a Qualifying Motor Vehicle" 
    unit = USD
    reference = "https://advance.lexis.com/documentpage/?pdmfid=1000516&crid=11477d83-e1a5-4c6c-9cf1-1987104961d3&action=pawlinkdoc&pdcomponentid=&pddocfullpath=%2Fshared%2Fdocument%2Fstatutes-legislation%2Furn%3AcontentItem%3A6894-01H3-GXF6-82SN-00008-00&pdtocnodeidentifier=ABPAACAACAABAAGABG&config=014FJAAyNGJkY2Y4Zi1mNjgyLTRkN2YtYmE4OS03NTYzNzYzOTg0OGEKAFBvZENhdGFsb2d592qv2Kywlf8caKqYROP5&ecomp=k2vckkk&prid=c6221a4f-589b-4907-bb54-7c3099e17ae4"
    # defined_for = "innovative_motor_vechicle_credit"
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        seating_cnt=tax_unit("innovative_motor_vehicle_passengers_seating", period)
        p = parameters(period).gov.states.co.tax.income.credits.innovative_motor_vehicle.eligibility
        meets_seating_requirement=seating_cnt<=p.max_passengers_seating
        classification = tax_unit("innovative_motor_vehicle_fuel_type", period)
        meets_fuel_type_requirement=p.innovative_motor_vehicle_fuel_type[classification]
        return (bool(meets_seating_requirement) & bool(meets_fuel_type_requirement))



