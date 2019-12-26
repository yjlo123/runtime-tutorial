## Introduction

Runtime Script is a tiny programming language I created for fun since early 2019.
Its syntax is assembly-like and greatly inspired by the game [Shenzhen IO](https://store.steampowered.com/app/504210/SHENZHEN_IO/).
Runtime Script is written in Javascript, so that it can be parsed and executed directly in the browser.

## Hello World
Just like any other programming language, the first program we are going to try is outputing a `Hello World` message.

Click the `Run` button below to run the `Hello World` program.

```runtime-embedded-box-0-100
prt 'Hello World!'
```


In the above embedded editor, you can write your program on the left and see the output of your program on the right after clicking the `Run` button.

To run the program one more time, just click the `Run` button again after the previous execution is finished.

To clear the console contents, you can click the console panel to focus on it, then type `clear` and press `Enter` key.

Let's get back to the program itself. The above `Hello World` program has just one line code, which has a keyword `prt` and a quoted string `'Hello World'`

```code-block
prt 'Hello World!'
```

In Runtime Script, we call such a line of code a `statement`.
Each statement has an instruction keyword, like `prt` in this example, and an arbitrary number of arguments. All the keywords and arguments are separated by spaces.


## Variables
To declare a variable, we use the `let` keyword, followed by the variable name and its value.
```code-block
let N V
```

A dollar sign (`$`) should be prepended to the variable name when it is referenced.

```runtime-embedded-box-0-140
let x 5
prt $x
let x 'abc'
prt $x
```

In the above example, we first create a new variable called `x` with an initial value of `5`, then print `x`. Now `x` is an integer.

Then we set a new value `'abc'`, which is a string, to the variable `x` and print it again.

## Data Types

In Runtime Script, there are only two primitive data types, i.e. integer (`int`) and string (`str`). Besides, there are another two advanced data types, `list` and `map`, details about these two data types will be explained in the Data Structure section.

We can check a variable or value's data type by using the `typ` instruction.
```code-block
typ N V
```

Also, we can convert integers to strings or strings to integers, using `str` and `int` respectively.
```code-block
int N V
str N V
```

```runtime-embedded-box-0-260
let x 5
let y '123'

typ tx $x
prt $tx

typ ty $y
prt $ty

int iy $y
add res $iy 1
prt $res
```


## Arithmetics
Runtime Script supports five basic arithmetic operations, namely addition (`add`), subtraction (`sub`), multiplication (`mul`), division (`div`), and modulo (`mod`).

```code-block
add N V V
sub N V V
mul N V V
div N V V
mod N V V
```

Let's take addition as an example, the sum of the two values `V V` is assigned to the variable `N`, the variable `N` will be created if it has not been defined.

The `div` instruction works as a floor division, thus the division result is always an integer.

Play around with the following examples to get familiar with these arithmetic operations.

```runtime-embedded-box-0-350
let x 5
let y 2

add z $x $y
prt $z

sub z $x $y
prt $z

mul z $x $y
prt $z

div z $x $y
prt $z

mod z $x $y
prt $z
```

Moreover, the arguments can be strings for the following cases:  
1. `add` two strings to concatenate them  
2. `add` a string/integer to an integer/string to concatenate them  
3. `mul` a string by an integer to repeate the string a number of times  

```runtime-embedded-box-0-200
add z 'Hello' 'World'
prt $z

add z 'abc' 5
prt $z

mul z 'Hi' 3
prt $z
```

## Jump

## Data Structures

## Miscellaneous

## Canvas

```runtime-embedded-box-1-250
clr
let x 9
#draw_dot
slp 200
drw $x 11 1
add x $x 2
jne $x 15 draw_dot
prt 'Hello World!'
```

## Advanced

