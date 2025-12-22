import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Packages Imports
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Assignment 1: Array Basics

    Hi there,

    Can you import Numpy and convert the following list comprehension (I just learned about comprehensions in an awesome course by Maven) into an array?

    Once you've done that report the following about the array:
    * The number of dimensions
    * The shape
    * The number of elements in the array
    * The type of data contained inside
    """)
    return


@app.cell
def _():
    my_list = [x * 10 for x in range(1, 11)]

    print(my_list)
    return (my_list,)


@app.cell
def _(my_list, np):
    array = np.array(my_list)

    print(array)
    return (array,)


@app.cell
def _(my_list):
    type(my_list)
    return


@app.cell
def _(array):
    type(array)
    return


@app.cell
def _(array):
    print(f"Number of dimensions: {array.ndim}")
    return


@app.cell
def _(array):
    print(f"Shape: {array.shape}")
    return


@app.cell
def _(array):
    print(f"Number of elements in the array: {array.size}")
    return


@app.cell
def _(array):
    print(f"Data type of each element: {array.dtype}")
    return


@app.cell
def _(array, mo):
    with mo.capture_stdout() as captured_output:
        _ = help(type(array))

    captured_value = captured_output.getvalue()
    return (captured_value,)


@app.cell
def _(captured_value):
    # First set of details of array help information
    first_block_pos = captured_value.find(" |  Parameters\n |  ----------")
    first_block = captured_value[:first_block_pos]
    remaining_block = captured_value[first_block_pos + 1 :]
    print(first_block)
    return (remaining_block,)


@app.cell
def _(remaining_block):
    # Parameters for the new method of Array class of numpy
    second_block_pos = remaining_block.find(" |  Attributes\n |  ----------")
    second_block = remaining_block[:second_block_pos]
    remaining_block_2 = remaining_block[second_block_pos + 1 :]
    print(second_block)
    return (remaining_block_2,)


@app.cell
def _(remaining_block_2):
    # Atributes for the new method of Array class of numpy
    third_block_pos = remaining_block_2.find("|  See Also\n |  --------")
    third_block = remaining_block_2[:third_block_pos]
    remaining_block_3 = remaining_block_2[third_block_pos + 1 :]
    print(third_block)
    return (remaining_block_3,)


@app.cell
def _(remaining_block_3):
    # "See also" section for the new method of Array class of numpy
    fourth_block_pos = remaining_block_3.find(" |  Notes\n |  -----")
    fourth_block = remaining_block_3[:fourth_block_pos]
    remaining_block_4 = remaining_block_3[fourth_block_pos + 1 :]
    _ = remaining_block_4
    print(fourth_block)
    return


if __name__ == "__main__":
    app.run()
