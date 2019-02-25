Feature:Water Over Flow

  Scenario Outline: Generate volume of the given glass in the row

  Given <volume> ml of liquid
  When poured  over a triangle of stacked glasess of <row> rows
  Then glass number <glass_number>  will have  <output_volume> volume in it

    Examples:
      | volume  | row | glass_number  | output_volume |
      |   250   |  0  |   0           |      250      |
      |   200   |  0  |   0           |      200      |
      |   500   |  1  |   1           |      125      |
      |   500   |  1  |   0           |      125      |
      |   1000  |  2  |   0           |      62.5     |
      |   1000  |  2  |   1           |      125      |
      |   1500  |  3  |   1           |      62.5     |
      |   1500  |  3  |   3           |      0        |