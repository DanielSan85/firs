"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='quarry',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['SAND', 'GRVL'],
                    layouts='AUTO',
                    prob_in_game='4',
                    prob_random='8',
                    prod_multiplier='[14, 14]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='195',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    # allow longer distance on clustering than usual, and more clusters, as industry is hard to locate
                    location_checks=IndustryLocationChecks(require_cluster=['quarry', [20, 90, 1, 4]],
                                                           incompatible={'brick_works': 16,
                                                                         'lime_kiln': 16,
                                                                         'glass_works': 16,
                                                                         'cement_plant': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_QUARRY)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_QUARRY))',
                    fund_cost_multiplier='210',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    template="refactor_primary_waterpit.pypnml" )

industry.economy_variations['FIRS'].enabled = True

# 2 tiles for this industry: pit outer tile cannot be on slopes; pit inner tiles and processor tiles can be
# cases for both tiles ensure that tiles can only be built at same height as north tile
industry.add_tile(id='quarry_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='quarry_tile_2',
		          foundations='return CB_RESULT_NO_FOUNDATIONS', # might not be needed, cargo-culted from previous code, didn't test; may be needed to stop rear foundations showing in some cases?
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

industry.add_industry_layout(
    id = 'quarry_layout_1',
    layout = [(0, 0, 'quarry_tile_2', 'quarry_spritelayout_24'),
              (0, 1, 'quarry_tile_2', 'quarry_spritelayout_18'),
              (0, 2, 'quarry_tile_2', 'quarry_spritelayout_12'),
              (0, 3, 'quarry_tile_2', 'quarry_spritelayout_6'),
              (1, 0, 'quarry_tile_2', 'quarry_spritelayout_23'),
              (1, 1, 'quarry_tile_1', 'quarry_spritelayout_17'),
              (1, 2, 'quarry_tile_1', 'quarry_spritelayout_11'),
              (1, 3, 'quarry_tile_2', 'quarry_spritelayout_5'),
              (2, 0, 'quarry_tile_2', 'quarry_spritelayout_22'),
              (2, 1, 'quarry_tile_1', 'quarry_spritelayout_16'),
              (2, 2, 'quarry_tile_1', 'quarry_spritelayout_10'),
              (2, 3, 'quarry_tile_2', 'quarry_spritelayout_4'),
              (3, 0, 'quarry_tile_2', 'quarry_spritelayout_20'),
              (3, 1, 'quarry_tile_1', 'quarry_spritelayout_14'),
              (3, 2, 'quarry_tile_1', 'quarry_spritelayout_8'),
              (3, 3, 'quarry_tile_2', 'quarry_spritelayout_2'),
              (4, 0, 'quarry_tile_2', 'quarry_spritelayout_19'),
              (4, 1, 'quarry_tile_2', 'quarry_spritelayout_13'),
              (4, 2, 'quarry_tile_2', 'quarry_spritelayout_7'),
              (4, 3, 'quarry_tile_2', 'quarry_spritelayout_1'),
              (6, 1, 'quarry_tile_1', 'quarry_spritelayout_41'),
              (6, 2, 'quarry_tile_1', 'quarry_spritelayout_37'),
              (7, 1, 'quarry_tile_1', 'quarry_spritelayout_40'),
              (7, 2, 'quarry_tile_1', 'quarry_spritelayout_36'),
              (8, 1, 'quarry_tile_1', 'quarry_spritelayout_39'),
              (8, 2, 'quarry_tile_1', 'quarry_spritelayout_35'),
    ]
)

industry.add_industry_layout(
    id = 'quarry_layout_2',
    layout = [(0, 3, 'quarry_tile_2', 'quarry_spritelayout_24'),
              (0, 4, 'quarry_tile_2', 'quarry_spritelayout_18'),
              (0, 5, 'quarry_tile_2', 'quarry_spritelayout_12'),
              (0, 6, 'quarry_tile_2', 'quarry_spritelayout_6'),
              (1, 1, 'quarry_tile_1', 'quarry_spritelayout_37'),
              (1, 0, 'quarry_tile_1', 'quarry_spritelayout_41'),
              (1, 3, 'quarry_tile_2', 'quarry_spritelayout_23'),
              (1, 4, 'quarry_tile_1', 'quarry_spritelayout_17'),
              (1, 5, 'quarry_tile_1', 'quarry_spritelayout_11'),
              (1, 6, 'quarry_tile_2', 'quarry_spritelayout_5'),
              (2, 0, 'quarry_tile_1', 'quarry_spritelayout_40'),
              (2, 1, 'quarry_tile_1', 'quarry_spritelayout_36'),
              (2, 3, 'quarry_tile_2', 'quarry_spritelayout_22'),
              (2, 4, 'quarry_tile_1', 'quarry_spritelayout_16'),
              (2, 5, 'quarry_tile_1', 'quarry_spritelayout_10'),
              (2, 6, 'quarry_tile_2', 'quarry_spritelayout_4'),
              (3, 0, 'quarry_tile_1', 'quarry_spritelayout_39'),
              (3, 1, 'quarry_tile_1', 'quarry_spritelayout_35'),
              (3, 3, 'quarry_tile_2', 'quarry_spritelayout_20'),
              (3, 4, 'quarry_tile_1', 'quarry_spritelayout_14'),
              (3, 5, 'quarry_tile_1', 'quarry_spritelayout_8'),
              (3, 6, 'quarry_tile_2', 'quarry_spritelayout_2'),
              (4, 3, 'quarry_tile_2', 'quarry_spritelayout_19'),
              (4, 4, 'quarry_tile_2', 'quarry_spritelayout_13'),
              (4, 5, 'quarry_tile_2', 'quarry_spritelayout_7'),
              (4, 6, 'quarry_tile_2', 'quarry_spritelayout_1'),
    ]
)

industry.add_industry_layout(
    id = 'quarry_layout_3',
    layout = [(0, 0, 'quarry_tile_2', 'quarry_spritelayout_24'),
              (0, 1, 'quarry_tile_2', 'quarry_spritelayout_18'),
              (0, 2, 'quarry_tile_2', 'quarry_spritelayout_12'),
              (0, 3, 'quarry_tile_2', 'quarry_spritelayout_6'),
              (1, 0, 'quarry_tile_2', 'quarry_spritelayout_23'),
              (1, 1, 'quarry_tile_1', 'quarry_spritelayout_17'),
              (1, 2, 'quarry_tile_1', 'quarry_spritelayout_11'),
              (1, 3, 'quarry_tile_2', 'quarry_spritelayout_5'),
              (1, 5, 'quarry_tile_1', 'quarry_spritelayout_41'),
              (1, 6, 'quarry_tile_1', 'quarry_spritelayout_37'),
              (2, 0, 'quarry_tile_2', 'quarry_spritelayout_22'),
              (2, 1, 'quarry_tile_1', 'quarry_spritelayout_16'),
              (2, 2, 'quarry_tile_1', 'quarry_spritelayout_10'),
              (2, 3, 'quarry_tile_2', 'quarry_spritelayout_4'),
              (2, 5, 'quarry_tile_1', 'quarry_spritelayout_40'),
              (2, 6, 'quarry_tile_1', 'quarry_spritelayout_36'),
              (3, 0, 'quarry_tile_2', 'quarry_spritelayout_20'),
              (3, 1, 'quarry_tile_1', 'quarry_spritelayout_14'),
              (3, 2, 'quarry_tile_1', 'quarry_spritelayout_8'),
              (3, 3, 'quarry_tile_2', 'quarry_spritelayout_2'),
              (3, 5, 'quarry_tile_1', 'quarry_spritelayout_39'),
              (3, 6, 'quarry_tile_1', 'quarry_spritelayout_35'),
              (4, 0, 'quarry_tile_2', 'quarry_spritelayout_19'),
              (4, 1, 'quarry_tile_2', 'quarry_spritelayout_13'),
              (4, 2, 'quarry_tile_2', 'quarry_spritelayout_7'),
              (4, 3, 'quarry_tile_2', 'quarry_spritelayout_1'),
    ]
)
