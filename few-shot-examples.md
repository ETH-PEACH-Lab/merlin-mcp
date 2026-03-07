# Tool Usage Guidelines for the Merlin MCP server

Merlin is a language to visualize algorithms.
The Merlin MCP returns the correct Merlin syntax for each method.

**General Rules:** If the user requests an entire algorithm to be visualised, show every computation step as follows:
Create a page with `create_page`
Go through all computation steps.
For every data structure that has not yet been shown, call `show_datastructure` with its variable name for `name`.

Comments are started with `//`.

The following examples show, given an algorithm to visualize, what Merlin code to generate:

**User Request:** "Given a 5 by 4 binary matrix where some cells are filled with zeros, show how an algorithm would calculate for each cell the distance to the nearest zero. The distance between two cells sharing an edge is 1."
**Tool use:**
Create a page with `create_page`
Define the matrix with `define_matrix` with matrix_name like `inputMatrix`, `value`
`[[" ", " ", " ", " "], [" ", 0, " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", 0, " "]]`
, color
`[[null, null, null, null], [null, "green", null, null], [null, 0, null, null], [null, null, null, null], [null, null, null, null], [null, null, 0, null]]`
and label it by setting `below` to `"Green = Current level"`.
Show this matrix on it by calling `show_datastructure` with `name` set to `inputMatrix`.
Create another page with `create_page`.
Go through the first algorithm step by calling `matrix_set_values` with `matrix_name` set to `inputMatrix` and `values` set to
`[[" ", 1, " ", " "], [1, 0, 1, " "], [" ", 1, " ", " "], [" ", " ", 1, " "], [" ", 1, 0, 1]]`.
Update the colors by calling `matrix_set_colors` with `matrix_name` set to `inputMatrix` and `colors` set to
`[[null, "green", null, null], ["green", null, "green", null], [null, "green", null, null], [null, null, "green", null], [null, "green", null, "green"]]`.
Create another page with `create_page`.
Go through the second algorithm step by calling `matrix_set_values` with `matrix_name` set to `inputMatrix` and `values` set to
`[[2, 1, 2, " "], [1, 0, 1, 2], [2, 1, 2, " "], [" ", 2, 1, 2], [2, 1, 0, 1]]`.
Update the colors by calling `matrix_set_colors` with `matrix_name` set to `inputMatrix` and `colors` set to
`[["green", null, "green", null], [null, null, null, "green"], ["green", null, "green", null], [null, "green", null, "green"], ["green", null, null, null]]`.
Create another page with `create_page`.
Go through the last algorithm step by calling `matrix_set_values` with `matrix_name` set to `inputMatrix` and `values` set to
`[[2, 1, 2, 3], [1, 0, 1, 2], [2, 1, 2, 3], [3, 2, 1, 2], [2, 1, 0, 1]]`.
Update the colors by calling `matrix_set_colors` with `matrix_name` set to `inputMatrix` and `colors` set to
`[[null, null, null, "green"], [null, null, null, null], [null, null, null, "green"], ["green", null, null, null], [null, null, null, null]]`.

**User Request:** "Show the 3SUM problem, finding values a, b, c with a + b = c, on the array [10, 7, 3, 22]"
**Tool use:**
Create a page with `create_page`.
Define the array by calling `define_array` with `array_name` `inputArray` and `value` `[10, 7, 3, 22]`.
Show this array by calling `show_datastructure` with `name` `inputArray`.
Create another page with `create_page`.
Sort the array by calling `array_set_values` with `array_name` `inputArray` and `value` `[3, 7, 10, 22]`.
Explain this step by calling `array_set_label` with `array_name` `inputArray`, `text` `Sort the array` and `position` `above`.
Create another page with `create_page`.
Set arrows by calling `array_set_arrows` with `array_name` `inputArray` and `["a", null, null, "b & c"]`.
Explain this step by calling `array_set_label` with `array_name` `inputArray`, `text` `Initialize a, b & c` and `position` `"above"`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `"a + b > c"` and `position` `above`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `None` and `position` `above`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `3` and `arrow` `c`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `2` and `arrow` `b`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `"a + b < c"` and `position` `above`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `None` and `position` `above`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `0` and `arrow` `None`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `1` and `arrow` `a`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `"a + b < c"` and `position` `above`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `None` and `position` `above`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `1` and `arrow` `None`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `2` and `arrow` `a & b`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `"a + b < c and a == b"` and `position` `above`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `None` and `position` `above`.
Call `array_set_arrows` with `array_name` `inputArray` and `arrows` `["a", null, "b & c", null]`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `a + b > c` and `position` `above`.
Create another page with `create_page`.
Call `array_set_label` with `array_name` `inputArray`, `text` `None` and `position` `above`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `2` and `arrow` `c`.
Call `array_set_arrow_at_index` with `array_name` `inputArray`, `index` `1` and `arrow` `b`.
