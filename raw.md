## Introduction

Runtime Script is a tiny programming language I created for fun since early 2019.
Its syntax is assembly-like and greatly inspired by the game [Shenzhen IO](https://store.steampowered.com/app/504210/SHENZHEN_IO/).
Runtime Script is written in Javascript, so that it can be parsed and executed directly in the browser.

## Hello World
Just like any other programming languages, the first program we are going to try is outputing a `Hello World` message.

Click the `Run` button below to run the `Hello World` program.

```runtime-embedded-box-0-90
/ Welcome to Runtime Script
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

The frist line in the above example is a comment, it is for your notation purpose and simply ignored by the execution. A comment starts with a slash (`/`), it can be after a statement with the same line or occupies the whole line.

## Variables
To declare a variable, we use the `let` keyword, followed by the variable name and its value.
```code-block
let N V
```

A dollar sign (`$`) should be prepended to the variable name when it is referenced.

```runtime-embedded-box-0-125
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

```runtime-embedded-box-0-280
let x 5
let y '123'

typ t_x $x
prt $t_x

typ t_y $y
prt $t_y

/ convert y from string to integer
int iy $y
typ t_iy $iy
prt $t_iy
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

```runtime-embedded-box-0-190
add z 'Hello' 'World'
prt $z

add z 'abc' 5
prt $z

mul z 'Hi' 3
prt $z
```

## Jump
In Runtime Script, you can insert labels to any places in your program, and jump to a specifc lable using the `jmp` instruction.
```code-block
jmp L
```
A label is a line starts with a hashtag `#`.

In the following example, the line `prt 'skipped'` is skipped because of jumping to the "continue" label.
```runtime-embedded-box-0-140
prt 'start'
jmp continue
prt 'skipped'
#continue
prt 'end'
```

There are four other jump instructions which only jump when a certain condition is true.

1. `jeq`: jump if equal  
2. `jne`: jump if not equal  
3. `jlt`: jump if less than  
4. `jgt`: jump if greater than  

```code-block
jeq V V L
jne V V L
jlt V V L
jgt V V L
```

```runtime-embedded-box-0-150
let i 0
#loop
prt $i
add i $i 1
jne $i 5 loop
```

The above example demonstrates printing and incrementing `i` from 0 to 4.

## Data Structures
Two data structures are provided in Runtime Script, i.e. `list` and `map`, and they are used as containers.

### List
The literal `[]` represents an empty list. Usually it is used when defining a new list.

> Defining a non-empty list is not supported.

There are three instructions for list operations:

```code-block
psh S V
pop S N
pol S N
```

`psh` for appending a value to the end to the list, `pop` for extracting the last item from the list, and `pol` for extracting the first item from the list.

```runtime-embedded-box-0-320
let list []
psh $list 3
psh $list 2
psh $list 'a'
prt $list

/ pop the last item
pop $list i
prt $i

/ poll the first item
pol $list j
prt $j

prt $list
```

> `pop` or `pol` from an empty list will result in a `nil`, which has the same value as the built-in constant `$nil`.

List instructions also work on strings. We can regard a string as a list and each character is an item in this list.

```runtime-embedded-box-0-200
let str 'abcz'

pop $str i
prt $i

psh $str 'd'
psh $str 'ef'
prt $str
```

> `pop` or `pol` from an empty stirng will result in an empty string (`''`).

### Map

The literal `{}` represents an empty map.

There are two instructions, `put` and `get`, for adding a key-value pair and getting the value by its key respectively.

```code-block
put M V V
get M V N
```

The keys are always strings, and the values can be any date types.

```runtime-embedded-box-0-300
let map {}

put $map 0 'Zero'
put $map 1 'One'
put $map 3 'Three'

let lst []
psh $lst 123

put $map list $lst

prt $map
get $map 3 val
prt $val
```

If you put a key-value pair where the key already exists in the map, the old value will be replaced with the new one.

```runtime-embedded-box-0-190
let map {}

put $map 0 'null'
put $map 1 'true'

put $map 0 'false'

prt $map
```

## Miscellaneous
### User input
Get a user input string from the console.
```code-block
inp N
```

```runtime-embedded-box-0-110
prt 'Enter your value:'
inp i
prt $i
```

### Sleep
Pause the program for a certain number of milliseconds.
```code-block
slp V
```

```runtime-embedded-box-0-110
prt 'Hello'
slp 1000
prt 'Bye'
```

In the above example, the program is paused for one second before printing the 'Bye' message.

In the following example, we are going to "slow-print" the hello wolrd message.

```runtime-embedded-box-0-230
let msg 'Hello, wrold!'

#next
pol $msg c
jeq $c '' done
slp 100
prt $c ''
jmp next
#done
prt ''
```

### Random
Get a random integer between two integers, where the second one is not included.
```code-block
rnd N V V
```

```runtime-embedded-box-0-110
/ Get a random integer among 1, 2, 3, 4
rnd num 1 5
prt $num
```

### Time
Get the system date or time.
```code-block
tim N year|month|date|day|hour|minute|second|milli
```

```runtime-embedded-box-0-90
tim y year
prt $y
```

### User Key Press
There is a special value, `lastkey`, which records the user's last pressed key code.
```runtime-embedded-box-0-300
prt 'Press an arrow key'
#start
let key $lastkey
slp 200
jeq $key -1 start

let key_map {}
put $key_map 37 'Left'
put $key_map 38 'Up'
put $key_map 39 'Right'
put $key_map 40 'Down'

get $key_map $key direction
prt $direction
```
You can check a specific key's code [here](https://keycode.info/).

## Canvas

```code-block
clr
drw V V V
pxl N V V
```

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
Runtime Script also has some advanced instructions to mimic some high-level programming language statements, such as if-else and functions. These instructions can make it more convenient to write programs, but we should use them with cautions.

### If-else
```code-block
ife V V
ifg V V
els
fin
```

> If-else cannot be nested!

### Function
```code-block
def N
ret
end
cal F
```

> Do not exit a function using jump statements.
