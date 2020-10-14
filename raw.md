## Introduction

Runtime Script is a tiny programming language I created for fun since early 2019.
Its syntax is assembly-like and greatly inspired by the game [Shenzhen IO](https://store.steampowered.com/app/504210/SHENZHEN_IO/).
Runtime Script is written in Javascript so that it can be parsed and executed directly in the browser.

Using Runtime Script, you can develop mini games (e.g. [Flappy Bird](https://runtime.siwei.dev/?src=bird)), solve algorithm problems (e.g. [Selection Sort](https://runtime.siwei.dev/?src=sort)), build wedgets (e.g. [Digital Clock](https://runtime.siwei.dev/?src=clock)), and do a lot more. (More examples [here](https://github.com/yjlo123/runtime-script#examples))

## Hello World
Just like any other programming language, the first program we are going to try is showing a `Hello World` message.

Click the `Run` button below to run the program.

```runtime-embedded-box-0-90
/ Welcome to Runtime Script
prt 'Hello World!'
```

In the embedded editor above, you can write your program on the left and see the output of your program on the right after clicking the `Run` button.

To run the program one more time, just click the `Run` button again after the previous execution is finished.

To clear the console contents, you can click the console panel to focus on it, then type `clear` and press `Enter` key.

Let's get back to the program itself. The above `Hello World` program has only one-line code, which contains a keyword `prt` and a quoted string `'Hello World'`.

```code-block
prt 'Hello World!'
```

In Runtime Script, we call such a line of code a `statement`.
Each statement has an instruction keyword, like `prt` in this example, and an arbitrary number of arguments. All the keywords and arguments are separated by spaces.

The first line in the above example is a comment, it is for your notation purpose and simply ignored by the evaluator. A comment starts with a slash (`/`), it can be after a statement with the same line or occupy the whole line.

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

In the above example, we firstly create a new variable called `x` with an initial value of `5`, then print `x`.

Then we set a new value `'abc'`, which is a string, to the variable `x` and print it again.

## Data Types

In Runtime Script, there are only two primitive data types, i.e. integer (`int`) and string (`str`). Besides, there are another two advanced data types, `list` and `map`, and details about these two will be explained in the Data Structure section.

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

Moreover, the argument can be non-integer for the following cases:  
1. `add` two strings to concatenate them  
2. `add` a string/integer to an integer/string to concatenate them  
3. `mul` a string by an integer to repeat the string certain times  
4. `add` `$nil` with an integer will convert this integer to a character (Decimal to ASCII)  
5. `sub` a character string by `$nil` will convert this character to an integer (ASCII to Decimal)  

```runtime-embedded-box-0-400
/ Case 1
add z 'Hello' 'World'
prt $z

/ Case 2
add z 'abc' 5
prt $z

/ Case 3
mul z 'Hi' 3
prt $z

/ Case 4
add z $nil 65
prt $z

/ Case 5
sub z 'A' $nil
prt $z
```

## Jump
In Runtime Script, you can insert labels to any places in your program and jump to a specific label using the `jmp` instruction.
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

Four other jump instructions only jump when a certain condition is true.

```code-block
jeq V V L
jne V V L
jlt V V L
jgt V V L
```

1. `jeq`: jump if V1 equals V2  
2. `jne`: jump if V1 is not equal to V2  
3. `jlt`: jump if V1 is less than V2  
4. `jgt`: jump if V1 is greater than V2  

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
The literal `[]` represents an empty list. Usually, it is used when defining a new list.

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

> `pop` or `pol` from an empty list will result in a `$nil`, which represents an empty value.

List instructions also work on strings. We can regard a string as a list and each character is an item in this list.

```runtime-embedded-box-0-200
let str 'abcz'

pop $str i		/ get last character
prt $i

psh $str 'd'	/ append a character to the end
psh $str 'ef'	/ append a string to the end
prt $str
```

> `pop` or `pol` from an empty string will result in an empty string (`''`).

### Map

The literal `{}` represents an empty map.

There are two instructions, `put` and `get`, for adding a key-value pair and getting the value by its key respectively.

```code-block
put M V V
get M V N
```

The keys are always strings, and the values can be any data types.

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

put $map 0 'zero'
put $map 1 'true'

put $map 0 'false'	/ update existing key's value

prt $map
```

If the key in the `get` statement does not present in the map, a `$nil` value will be returned.

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
slp 1000	/ 1000 milliseconds (1 second)
prt 'Bye'
```

In the above example, the program is paused for one second before printing the 'Bye' message.

In the following example, we are going to "slow-print" the hello world message.

```runtime-embedded-box-0-230
let msg 'Hello, world!'

#next
pol $msg c
jeq $c '' done
slp 100
prt $c ''
jmp next
#done
prt ''
```

You may find that the first `prt` has two arguments, the first one is the content to be printed, while the second one is the terminator character, which is optional and is a newline character by default.

In the above example, we are trying to print each character in the same line, thus we indicate the terminator as an empty string.

### Random
Get a random integer between two integers, where the ending integer is not included.
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
There is a special value, `$lastkey`, which records the user's last pressed key code.
```runtime-embedded-box-0-310
prt 'Press an arrow key'
#start
let key $lastkey
slp 200
jeq $key -1 start	/ $lastkey is -1 if user pressed nothing

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

Runtime Script natively supports a canvas for displaying graphics. The default canvas is a 24-by-24 pixel matrix.

```runtime-embedded-box-3-170
drw 0 0 1
```

You can find there is a black area on the right of the above editor. After clicking the `run` button, you will see a white dot drawn on the top-left corner.

The origin of the canvas is at the top-left, and column/row numbers are zero-based.

For instance, `drw 0 2 1` means filling the dot on column 0 (1st column) row 2 (3rd row) with white (`1`).

The supported instructions for canvas operations are:
```code-block
clr
drw V V V
pxl N V V
```

1. `clr`: clear the canvas, in other words, fill the whole canvas with black
2. `drw`: fill the pixel at (V1, V2) with color V3
3. `pxl`: get the color of the pixel (V1, V2)

The canvas and console can work together, in the following example, it prints three dots on the canvas with a 0.2-second interval, then prints the 'Hello World!' in the console.

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

Runtime Script canvas suppots 16 colors.

```runtime-embedded-box-3-340
drw 0 0 0	/ black
drw 0 1 1	/ white
drw 0 2 2	/ yellow
drw 0 3 3	/ orange
drw 0 4 4	/ red
drw 0 5 5	/ magenta
drw 0 6 6	/ purple
drw 0 7 7	/ blue
drw 0 8 8	/ cyan
drw 0 9 9	/ green
drw 0 10 10	/ dark green
drw 0 11 11	/ brown
drw 0 12 12	/ tan
drw 0 13 13	/ silver (light gray)
drw 0 14 14	/ gray (medium gray)
drw 0 15 15	/ dark gray
```

## Advanced
Runtime Script also has some advanced instructions to mimic some high-level programming language statements, such as if-else and functions. These instructions can make it more convenient to write programs, but we should use them with caution.

> Indentations in Runtime Script are only for readability, they do not affect the execution.

### If-else
Executing certain lines of statements depends on the comparison result of two values.
```code-block
ife V V
ifg V V
els
fin
```

1. `ife`: if V1 equals V2, execute the statements below until `els` or `fin` encountered
2. `ifg`: similar to `ife`, but check if V1 is greater than V2 instead
3. `els`: (optional) if the above condition is false, execute the statements below until `fin` encountered
4. `fin`: the end of if-else

> Nested if-else is not supported.

If-else is a convenient way to write condition checks, it may save your time writing complicated codes with jumps and labels.

The following program checking the equality of two numbers by using `if-else`
```runtime-embedded-box-0-180
let a 0
let b 1
ife $a $b
 prt 'equal'
els
 prt 'not equal'
fin
```
is equivalent to
```runtime-embedded-box-0-200
let a 0
let b 1
jne $a $b not_equal
prt 'equal'
jmp end_check
#not_equal
prt 'not equal'
#end_check
```

### Function
Defining a block of statements for code reuse.
```code-block
def F
ret
end
cal F
```

1. `def`: the head of a function definition with a name
2. `ret`: jump to the line below the previous function call
3. `end`: the end of the function definition, jump to the line below the previous function call
4. `cal`: jump to the function head by name

> Do not use jump statements to exit a function.

> The function code blocks in Runtime Script are actually pseudo funtions, they do not have a scopped variable namespace or a closure environment, that means, all the variables declared or used in the functions are global.

In the example below, a 'random' function is defined and then invoked twice. 
```runtime-embedded-box-0-190
def random
 prt 'Your random number:'
 rnd n 1 10
 prt $n
end

cal random
cal random
```

You can invoke a function inside a function.
```runtime-embedded-box-0-260
def func_a
 prt '== A start'
 cal func_b
 prt '== A end'
end

def func_b
 prt '** B start'
 prt '** B end'
end

cal func_a
```

Recursion is supported. The following program demonstrates the recursive version of calculating factorials.
```runtime-embedded-box-0-470
def factorial
 pop $s n
 ife $n 1		/ base case
  psh $s $n
  ret			/ return to last func call
 fin
 psh $s $n
 sub n1 $n 1	/ decrease param by 1
 psh $s $n1		/ param for recursion call

 cal factorial	/ recursion call

 pop $s n3
 pop $s n4		/ pop 2 nums from stack
 mul n5 $n3 $n4	/ get their product
 psh $s $n5		/ push back to stack
end

let num 5
let s []		/ a temp param stack
psh $s $num
cal factorial	/ initial func call
pop $s res		/ only 1 num left in stack
prt $res
```

You may wonder if the functions in Runtime Script can accept arguments, the answer is yes. You can pass primitive values (integers and strings only) to the function you are calling, and get these values in the function by indexing ($0, $1, $2 and so on).

```runtime-embedded-box-0-210
def func
 prt $0
 prt $1
end

cal func 5 "abc"

/ undefined outside the function
prt $0
```
