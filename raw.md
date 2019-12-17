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

To clear the console contents, you can click the console panel to focus on it, then type `clear` and press Enter.

Let's get back to the program itself. The above `Hello World` program has just one line code, which has a keyword `prt` and a quotated string `'Hello World'`

```code-block
prt 'Hello World!'
```

In Runtime Script, we call such a line of code a `statement`.
Each statement has an instruction keyword, like `prt` in this example, and an arbitrary number of arguments. All the keywords and arguments are separated by a space.


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

In Runtime Script, there are only two primitive data types, i.e. integer (`int`) and string (`str`).


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

## Arithmetics

## Jump
