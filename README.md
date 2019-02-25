# Plexus-Coding-Challenge
Solution to the Plexus code chalenge

## Table of contents:

* [Description](./README.md#description)
  * [Constraints](./README.md#constraints)
  * [Example Input and Output](./README.md#example-input-and-output)
  * [Deliverables](./README.md#deliverables)
* [Setup](./README.md#setup)
* [Running the app](./README.md#running-the-app)
* [Running the tests](./README.md#running-the-tests)
* [Considerations about the development](./README.md#considerations-about-the-development)
* [Examples of use](./src/features/waterOverFlow.feature)

## Description

* There is a stack of water glasses in a form of triangle. Each glass has a 250ml capacity.
When a liquid is poured into the top most glass any overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass.

### Constraints

* The glass in the row to be seleted to find the volume must me lessa than or equal to the number of rows of the stack.

### Example Input and Output:

#### Example

  ```python3 handler.py -k 250 -i 0 -j 0```
Expected output
For volume: 250 ml   rows: 0     glass : 0
result :  {
  "output": 250,
  "validation_message": "Valid input",
  "validation_status": "SUCCESSFUL"
}

### Deliverables

Source code, and any test code/data used in developing the solution.

## Setup

1. Make sure you have Python3 installed on your machine. If you need help installing , take a look at the [installation guide](https://realpython.com/installing-python/).

2. Clone this repo:

    ```git clone git@github.com:nabilyusuf/Plexus-Coding-Challenge.git```

3. Change to the src directory:

    ```cd Plexus-Cooding-Challenge/src```

4. Install dependencies:

    ```pip3 install -r requirement.txt```

And you're ready to go!

### Running the app:
```python3 handler.py```

### Running the test:

```cd features```
```behave```

### Considerations about the development:

* Since the application is about calculating the volume of glasses arraged in a triang1led stack. This problem can be solved by considering that every top glass fills the bottom 2 glasss which support it when its overflowed.

* This follows the [pascal triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)pattern, but since we start from the zero row and zero glass, the equation didn't seem to work. to overcome this problem, I incremented the input