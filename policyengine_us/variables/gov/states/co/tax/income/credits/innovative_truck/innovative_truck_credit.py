from policyengine_us.model_api import *


class innovative_truck_credit(Variable):
    value_type = float
    entity = TaxUnit
    definition_period = YEAR
    label = "Colorado innovative truck credit"
    documentation = "Credit of Purchase or Lease a Qualifying Innovative truck"
    unit = USD
    reference = "https://advance.lexis.com/documentpage/?pdmfid=1000516&crid=53a5e947-1990-4f4a-b74a-e4bc4de1668f&action=pawlinkdoc&pdcomponentid=&pddocfullpath=%2Fshared%2Fdocument%2Fstatutes-legislation%2Furn%3AcontentItem%3A6894-0703-GXF6-837P-00008-00&pdtocnodeidentifier=ABPAACAACAABAAGABH&config=014FJAAyNGJkY2Y4Zi1mNjgyLTRkN2YtYmE4OS03NTYzNzYzOTg0OGEKAFBvZENhdGFsb2d592qv2Kywlf8caKqYROP5&ecomp=k2vckkk&prid=11477d83-e1a5-4c6c-9cf1-1987104961d3"
    defined_for = "innovative_truck_credit_eligible"

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.co.tax.income.credits.innovative_truck
        ownership = tax_unit("innovative_vehicle_ownership", period)
        possible_ownership = ownership.possible_values
        gvwr = tax_unit("gross_vehicle_weight_rating", period)
        return select(
            [
                ownership == possible_ownership.OTHER,
                ownership == possible_ownership.VECHICLE_LEASE,
                ownership == possible_ownership.VECHICLE_PURCHASE,
            ],
            [
                0,
                p.lease.calc(gvwr),
                p.purchase.calc(gvwr),
            ],
        )
