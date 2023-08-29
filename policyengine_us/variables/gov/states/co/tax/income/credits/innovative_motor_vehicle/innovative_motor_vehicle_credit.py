from policyengine_us.model_api import *


class innovative_motor_vehicle_credit(Variable):
    value_type = float
    entity = TaxUnit
    definition_period = YEAR
    label = "Colorado innovative motor vechicle credit"
    documentation = (
        "Credit of Purchase or Lease a Qualifying Innovative Motor Vehicle"
    )
    unit = USD
    reference = "https://advance.lexis.com/documentpage/?pdmfid=1000516&crid=11477d83-e1a5-4c6c-9cf1-1987104961d3&action=pawlinkdoc&pdcomponentid=&pddocfullpath=%2Fshared%2Fdocument%2Fstatutes-legislation%2Furn%3AcontentItem%3A6894-01H3-GXF6-82SN-00008-00&pdtocnodeidentifier=ABPAACAACAABAAGABG&config=014FJAAyNGJkY2Y4Zi1mNjgyLTRkN2YtYmE4OS03NTYzNzYzOTg0OGEKAFBvZENhdGFsb2d592qv2Kywlf8caKqYROP5&ecomp=k2vckkk&prid=c6221a4f-589b-4907-bb54-7c3099e17ae4"
    defined_for = "innovative_motor_vechicle_credit_eligible"

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.co.tax.income.credits.innovative_motor_vehicle
        ownership = tax_unit("innovative_vehicle_ownership", period)
        innovative_motor_vehicle_credit = p.amount[ownership]
        return innovative_motor_vehicle_credit
