Feature:Water Over Flow 

  Scenario Outline: Generate volume of the overflow glass 

  Given <k> ml of liquid poured  over stack of glasess 
  When <i> row of the <j> glass
  Then I should volume as <output>

    Examples:
      |k  | i | j |output|
      | 500 | 1 | 1 | 250    |