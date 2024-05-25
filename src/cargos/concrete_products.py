from cargo import Cargo

cargo = Cargo(
    id="concrete_products",
    type_name="string(STR_CARGO_NAME_CONCRETE_PRODUCTS)",
    unit_name="string(STR_CARGO_NAME_CONCRETE_PRODUCTS)",
    type_abbreviation="string(STR_CID_CONCRETE_PRODUCTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="CCPR",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CONCRETE_PRODUCTS)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    price_factor=150,
    capacity_multiplier="1",
    icon_indices=(5, 6),
    sprites_complete=True,
)
