from behave import *

@given('{k} ml of liquid poured  over stack of glasess')
def step_impl(context,k):
    assert  k == "1"

@when('{i} row of the {j} glass')
def step_impl(context,i,j):
    assert  i == "2" 
    assert  j == "3"
    context.result = i

@then('I should volume as {output}')
def step_impl(context,output):
    assert  output == context.result 

