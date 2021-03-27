from cargo import Cargo

cargo = Cargo(
    id="stainless_steel",
    type_name="string(STR_CARGO_NAME_STAINLESS_STEEL)",
    unit_name="string(STR_CARGO_NAME_STAINLESS_STEEL)",
    type_abbreviation="string(STR_CID_STAINLESS_STEEL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="STST",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STAINLESS_STEEL)",
    penalty_lowerbound="16",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=130,
    icon_indices=(10, 4),
)
