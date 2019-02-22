from behave import *
import handler

@given('{k} ml of liquid poured  over stack of glasess')
def step_impl(context,k):
    context.k = int(k)
    pass

@when('{i} row of the {j} glass')
def step_impl(context,i,j):
    context.i = int(i)
    context.j = int(j)
    pass

@then('I should volume as {output}')
def step_impl(context,output):
    result = handler.setupRun(context.k,context.i,context.j)["output"]
    print(result)

