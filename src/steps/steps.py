from behave import *
import handler

@given('{vol} ml of liquid')
def step_impl(context,vol):
    context.vol = int(vol)
    pass

@when('poured  over a triangle of stacked glasess of {row} rows')
def step_impl(context,row):
    context.rows = int(row)
    pass

@then('glass number {glass_number}  will have  {output_volume} volume in it')
def step_impl(context,glass_number, output_volume):
    context.result = handler.setupRun(context.vol,context.rows,int(glass_number))["output"]
    # assert_that(context.result, equal_to(output))
    assert ( float(context.result) == float(output_volume))

