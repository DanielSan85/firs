from industry import IndustryPrimaryNoSupplies, TileLocationChecks

industry = IndustryPrimaryNoSupplies(id='fishing_grounds',
                                     accept_cargo_types=[],
                                     prod_cargo_types_with_multipliers=[('FISH', 7)],
                                     prob_in_game='14',
                                     prob_random='14',
                                     substitute='5',
                                     map_colour='160',
                                     life_type='IND_LIFE_TYPE_EXTRACTIVE',
                                     special_flags=['IND_FLAG_BUILT_ON_WATER', 'IND_FLAG_NO_PRODUCTION_INCREASE', 'IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES'],
                                     location_checks=dict(cluster=[60, 5],
                                                          coast_distance=True),
                                     prospect_chance='0.75',
                                     name='string(STR_IND_FISHING_GROUND)',
                                     nearby_station_name='string(STR_STATION_SHOALS)',
                                     fund_cost_multiplier='88')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
#industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True

industry.add_tile(id='fishing_grounds_tile_1',
                  location_checks=TileLocationChecks(disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDSPRITE_WATER',
)
spriteset_ground_empty = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 31, -31, 0)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 31, -31, 0)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 31, -31, 0)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 31, -31, -32)],
)

industry.add_spritelayout(
    id='fishing_grounds_spritelayout_1',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_1]
)
industry.add_spritelayout(
    id='fishing_grounds_spritelayout_2',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_2]
)
industry.add_spritelayout(
    id='fishing_grounds_spritelayout_3',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_3]
)
industry.add_spritelayout(
    id='fishing_grounds_spritelayout_4',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_5,
    building_sprites=[spriteset_4]
)
industry.add_spritelayout(
    id='fishing_grounds_spritelayout_null',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[]
)

industry.add_industry_layout(
    id='fishing_grounds_industry_layout_1',
    layout=[(0, 0, '255', 'fishing_grounds_spritelayout_null'),
            (0, 1, '255', 'fishing_grounds_spritelayout_null'),
            (0, 2, '255', 'fishing_grounds_spritelayout_null'),
            (0, 3, '255', 'fishing_grounds_spritelayout_null'),
            (0, 4, '255', 'fishing_grounds_spritelayout_null'),
            (0, 5, '255', 'fishing_grounds_spritelayout_null'),
            (0, 6, '255', 'fishing_grounds_spritelayout_null'),
            (1, 0, '255', 'fishing_grounds_spritelayout_null'),
            (1, 1, '255', 'fishing_grounds_spritelayout_null'),
            (1, 2, '255', 'fishing_grounds_spritelayout_null'),
            (1, 3, '255', 'fishing_grounds_spritelayout_null'),
            (1, 4, '255', 'fishing_grounds_spritelayout_null'),
            (1, 5, '255', 'fishing_grounds_spritelayout_null'),
            (1, 6, '255', 'fishing_grounds_spritelayout_null'),
            (2, 0, '255', 'fishing_grounds_spritelayout_null'),
            (2, 1, '255', 'fishing_grounds_spritelayout_null'),
            (2, 2, '24', 'fishing_grounds_spritelayout_null'),
            (2, 3, '24', 'fishing_grounds_spritelayout_null'),
            (2, 4, '255', 'fishing_grounds_spritelayout_null'),
            (2, 5, '255', 'fishing_grounds_spritelayout_null'),
            (2, 6, '255', 'fishing_grounds_spritelayout_null'),
            (3, 0, '255', 'fishing_grounds_spritelayout_null'),
            (3, 1, '255', 'fishing_grounds_spritelayout_null'),
            (3, 2, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_1'),
            (3, 3, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_4'),
            (3, 4, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_2'),
            (3, 5, '255', 'fishing_grounds_spritelayout_null'),
            (3, 6, '255', 'fishing_grounds_spritelayout_null'),
            (4, 0, '255', 'fishing_grounds_spritelayout_null'),
            (4, 1, '255', 'fishing_grounds_spritelayout_null'),
            (4, 2, '255', 'fishing_grounds_spritelayout_null'),
            (4, 3, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_3'),
            (4, 4, '255', 'fishing_grounds_spritelayout_null'),
            (4, 5, '255', 'fishing_grounds_spritelayout_null'),
            (4, 6, '255', 'fishing_grounds_spritelayout_null'),
            (5, 0, '255', 'fishing_grounds_spritelayout_null'),
            (5, 1, '255', 'fishing_grounds_spritelayout_null'),
            (5, 2, '255', 'fishing_grounds_spritelayout_null'),
            (5, 3, '255', 'fishing_grounds_spritelayout_null'),
            (5, 4, '255', 'fishing_grounds_spritelayout_null'),
            (5, 5, '255', 'fishing_grounds_spritelayout_null'),
            (5, 6, '255', 'fishing_grounds_spritelayout_null'),
            (6, 0, '255', 'fishing_grounds_spritelayout_null'),
            (6, 1, '255', 'fishing_grounds_spritelayout_null'),
            (6, 2, '255', 'fishing_grounds_spritelayout_null'),
            (6, 3, '255', 'fishing_grounds_spritelayout_null'),
            (6, 4, '255', 'fishing_grounds_spritelayout_null'),
            (6, 5, '255', 'fishing_grounds_spritelayout_null'),
            (6, 6, '255', 'fishing_grounds_spritelayout_null'),
            ]
)
industry.add_industry_layout(
    id='fishing_grounds_industry_layout_2',
    layout=[(0, 0, '255', 'fishing_grounds_spritelayout_null'),
            (0, 1, '255', 'fishing_grounds_spritelayout_null'),
            (0, 2, '255', 'fishing_grounds_spritelayout_null'),
            (0, 3, '255', 'fishing_grounds_spritelayout_null'),
            (0, 4, '255', 'fishing_grounds_spritelayout_null'),
            (0, 5, '255', 'fishing_grounds_spritelayout_null'),
            (0, 6, '255', 'fishing_grounds_spritelayout_null'),
            (1, 0, '255', 'fishing_grounds_spritelayout_null'),
            (1, 1, '255', 'fishing_grounds_spritelayout_null'),
            (1, 2, '255', 'fishing_grounds_spritelayout_null'),
            (1, 3, '255', 'fishing_grounds_spritelayout_null'),
            (1, 4, '255', 'fishing_grounds_spritelayout_null'),
            (1, 5, '255', 'fishing_grounds_spritelayout_null'),
            (1, 6, '255', 'fishing_grounds_spritelayout_null'),
            (2, 0, '255', 'fishing_grounds_spritelayout_null'),
            (2, 1, '255', 'fishing_grounds_spritelayout_null'),
            (2, 2, '255', 'fishing_grounds_spritelayout_null'),
            (2, 3, '24', 'fishing_grounds_spritelayout_null'),
            (2, 4, '24', 'fishing_grounds_spritelayout_null'),
            (2, 5, '255', 'fishing_grounds_spritelayout_null'),
            (2, 6, '255', 'fishing_grounds_spritelayout_null'),
            (3, 0, '255', 'fishing_grounds_spritelayout_null'),
            (3, 1, '255', 'fishing_grounds_spritelayout_null'),
            (3, 2, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_1'),
            (3, 3, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_2'),
            (3, 4, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_4'),
            (3, 5, '255', 'fishing_grounds_spritelayout_null'),
            (3, 6, '255', 'fishing_grounds_spritelayout_null'),
            (4, 0, '255', 'fishing_grounds_spritelayout_null'),
            (4, 1, '255', 'fishing_grounds_spritelayout_null'),
            (4, 2, '255', 'fishing_grounds_spritelayout_null'),
            (4, 3, '255', 'fishing_grounds_spritelayout_null'),
            (4, 4, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_3'),
            (4, 5, '255', 'fishing_grounds_spritelayout_null'),
            (4, 6, '255', 'fishing_grounds_spritelayout_null'),
            (5, 0, '255', 'fishing_grounds_spritelayout_null'),
            (5, 1, '255', 'fishing_grounds_spritelayout_null'),
            (5, 2, '255', 'fishing_grounds_spritelayout_null'),
            (5, 3, '255', 'fishing_grounds_spritelayout_null'),
            (5, 4, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_3'),
            (5, 5, '255', 'fishing_grounds_spritelayout_null'),
            (5, 6, '255', 'fishing_grounds_spritelayout_null'),
            (6, 0, '255', 'fishing_grounds_spritelayout_null'),
            (6, 1, '255', 'fishing_grounds_spritelayout_null'),
            (6, 2, '255', 'fishing_grounds_spritelayout_null'),
            (6, 3, '255', 'fishing_grounds_spritelayout_null'),
            (6, 4, '255', 'fishing_grounds_spritelayout_null'),
            (6, 5, '255', 'fishing_grounds_spritelayout_null'),
            (6, 6, '255', 'fishing_grounds_spritelayout_null'),
            (7, 0, '255', 'fishing_grounds_spritelayout_null'),
            (7, 1, '255', 'fishing_grounds_spritelayout_null'),
            (7, 2, '255', 'fishing_grounds_spritelayout_null'),
            (7, 3, '255', 'fishing_grounds_spritelayout_null'),
            (7, 4, '255', 'fishing_grounds_spritelayout_null'),
            (7, 5, '255', 'fishing_grounds_spritelayout_null'),
            (7, 6, '255', 'fishing_grounds_spritelayout_null'),
            ]
)
industry.add_industry_layout(
    id='fishing_grounds_industry_layout_3',
    layout=[(0, 0, '255', 'fishing_grounds_spritelayout_null'),
            (0, 1, '255', 'fishing_grounds_spritelayout_null'),
            (0, 2, '255', 'fishing_grounds_spritelayout_null'),
            (0, 3, '255', 'fishing_grounds_spritelayout_null'),
            (0, 4, '255', 'fishing_grounds_spritelayout_null'),
            (0, 5, '255', 'fishing_grounds_spritelayout_null'),
            (0, 6, '255', 'fishing_grounds_spritelayout_null'),
            (1, 0, '255', 'fishing_grounds_spritelayout_null'),
            (1, 1, '255', 'fishing_grounds_spritelayout_null'),
            (1, 2, '255', 'fishing_grounds_spritelayout_null'),
            (1, 3, '255', 'fishing_grounds_spritelayout_null'),
            (1, 4, '255', 'fishing_grounds_spritelayout_null'),
            (1, 5, '255', 'fishing_grounds_spritelayout_null'),
            (1, 6, '255', 'fishing_grounds_spritelayout_null'),
            (2, 0, '255', 'fishing_grounds_spritelayout_null'),
            (2, 1, '255', 'fishing_grounds_spritelayout_null'),
            (2, 2, '255', 'fishing_grounds_spritelayout_null'),
            (2, 3, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_3'),
            (2, 4, '255', 'fishing_grounds_spritelayout_null'),
            (2, 5, '255', 'fishing_grounds_spritelayout_null'),
            (2, 6, '255', 'fishing_grounds_spritelayout_null'),
            (3, 0, '255', 'fishing_grounds_spritelayout_null'),
            (3, 1, '255', 'fishing_grounds_spritelayout_null'),
            (3, 2, '255', 'fishing_grounds_spritelayout_null'),
            (3, 3, '255', 'fishing_grounds_spritelayout_null'),
            (3, 4, '255', 'fishing_grounds_spritelayout_null'),
            (3, 5, '255', 'fishing_grounds_spritelayout_null'),
            (3, 6, '255', 'fishing_grounds_spritelayout_null'),
            (4, 0, '255', 'fishing_grounds_spritelayout_null'),
            (4, 1, '255', 'fishing_grounds_spritelayout_null'),
            (4, 2, '24', 'fishing_grounds_spritelayout_null'),
            (4, 3, '24', 'fishing_grounds_spritelayout_null'),
            (4, 4, '255', 'fishing_grounds_spritelayout_null'),
            (4, 5, '255', 'fishing_grounds_spritelayout_null'),
            (4, 6, '255', 'fishing_grounds_spritelayout_null'),
            (5, 0, '255', 'fishing_grounds_spritelayout_null'),
            (5, 1, '255', 'fishing_grounds_spritelayout_null'),
            (5, 2, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_2'),
            (5, 3, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_4'),
            (5, 4, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_2'),
            (5, 5, '255', 'fishing_grounds_spritelayout_null'),
            (5, 6, '255', 'fishing_grounds_spritelayout_null'),
            (6, 0, '255', 'fishing_grounds_spritelayout_null'),
            (6, 1, '255', 'fishing_grounds_spritelayout_null'),
            (6, 2, '255', 'fishing_grounds_spritelayout_null'),
            (6, 3, '255', 'fishing_grounds_spritelayout_null'),
            (6, 4, '255', 'fishing_grounds_spritelayout_null'),
            (6, 5, '255', 'fishing_grounds_spritelayout_null'),
            (6, 6, '255', 'fishing_grounds_spritelayout_null'),
            (7, 0, '255', 'fishing_grounds_spritelayout_null'),
            (7, 1, '255', 'fishing_grounds_spritelayout_null'),
            (7, 2, '255', 'fishing_grounds_spritelayout_null'),
            (7, 3, '255', 'fishing_grounds_spritelayout_null'),
            (7, 4, '255', 'fishing_grounds_spritelayout_null'),
            (7, 5, '255', 'fishing_grounds_spritelayout_null'),
            (7, 6, '255', 'fishing_grounds_spritelayout_null'),
            ]
)
industry.add_industry_layout(
    id='fishing_grounds_industry_layout_4',
    layout=[(0, 0, '255', 'fishing_grounds_spritelayout_null'),
            (0, 1, '255', 'fishing_grounds_spritelayout_null'),
            (0, 2, '255', 'fishing_grounds_spritelayout_null'),
            (0, 3, '255', 'fishing_grounds_spritelayout_null'),
            (0, 4, '255', 'fishing_grounds_spritelayout_null'),
            (0, 5, '255', 'fishing_grounds_spritelayout_null'),
            (0, 6, '255', 'fishing_grounds_spritelayout_null'),
            (1, 0, '255', 'fishing_grounds_spritelayout_null'),
            (1, 1, '255', 'fishing_grounds_spritelayout_null'),
            (1, 2, '255', 'fishing_grounds_spritelayout_null'),
            (1, 3, '255', 'fishing_grounds_spritelayout_null'),
            (1, 4, '255', 'fishing_grounds_spritelayout_null'),
            (1, 5, '255', 'fishing_grounds_spritelayout_null'),
            (1, 6, '255', 'fishing_grounds_spritelayout_null'),
            (2, 0, '255', 'fishing_grounds_spritelayout_null'),
            (2, 1, '255', 'fishing_grounds_spritelayout_null'),
            (2, 2, '24', 'fishing_grounds_spritelayout_null'),
            (2, 3, '24', 'fishing_grounds_spritelayout_null'),
            (2, 4, '255', 'fishing_grounds_spritelayout_null'),
            (2, 5, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_3'),
            (2, 6, '255', 'fishing_grounds_spritelayout_null'),
            (3, 0, '255', 'fishing_grounds_spritelayout_null'),
            (3, 1, '255', 'fishing_grounds_spritelayout_null'),
            (3, 2, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_2'),
            (3, 3, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_4'),
            (3, 4, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_3'),
            (3, 5, 'fishing_grounds_tile_1', 'fishing_grounds_spritelayout_1'),
            (3, 6, '255', 'fishing_grounds_spritelayout_null'),
            (4, 0, '255', 'fishing_grounds_spritelayout_null'),
            (4, 1, '255', 'fishing_grounds_spritelayout_null'),
            (4, 2, '255', 'fishing_grounds_spritelayout_null'),
            (4, 3, '255', 'fishing_grounds_spritelayout_null'),
            (4, 4, '255', 'fishing_grounds_spritelayout_null'),
            (4, 5, '255', 'fishing_grounds_spritelayout_null'),
            (4, 6, '255', 'fishing_grounds_spritelayout_null'),
            (5, 0, '255', 'fishing_grounds_spritelayout_null'),
            (5, 1, '255', 'fishing_grounds_spritelayout_null'),
            (5, 2, '255', 'fishing_grounds_spritelayout_null'),
            (5, 3, '255', 'fishing_grounds_spritelayout_null'),
            (5, 4, '255', 'fishing_grounds_spritelayout_null'),
            (5, 5, '255', 'fishing_grounds_spritelayout_null'),
            (5, 6, '255', 'fishing_grounds_spritelayout_null'),
            ]
)
