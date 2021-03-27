from cargo import Cargo

cargo = Cargo(
    id="fruits",
    type_name="string(STR_CARGO_NAME_FRUITS)",
    unit_name="string(STR_CARGO_NAME_FRUITS)",
    type_abbreviation="TTD_STR_ABBREV_FRUIT",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_EXPRESS, CC_PIECE_GOODS, CC_REFRIGERATED)",
    cargo_label="FRUT",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FRUITS)",
    penalty_lowerbound="0",
    single_penalty_length="26",
    price_factor=124,
    capacity_multiplier="1",
    icon_indices=(14, 0),
)
