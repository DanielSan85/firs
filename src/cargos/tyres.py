from cargo import Cargo

cargo = Cargo(
    id="tyres",
    type_name="string(STR_CARGO_NAME_TYRES)",
    unit_name="string(STR_CARGO_NAME_TYRES)",
    type_abbreviation="string(STR_CID_TYRES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="TYRE",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_TYRES)",
    penalty_lowerbound="8",
    single_penalty_length="255",
    price_factor=149,
    capacity_multiplier="1",
    icon_indices=(7, 4),
)
