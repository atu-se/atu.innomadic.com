Some Token Types from a Typical Language

Type   | Examples
-------|-------------------------------
ID     | foo n14 last
NUM    | 73 0 00 515 082
REAL   | 66.1 .5 10. 1e67 5.5e-10 IF if
COMMA  | ,
NOTEQ  | !=
LPAREN | (
RPAREN | )

# Non-Tokens

Type                       | Example
---------------------------|-------------------
comment                    | /* try again */
preprocessor directive     | #include<stdio.h>
preprocessor directive     | #define NUMS 5 , 6
macro                      | NUMS
blanks, tabs, and newlines |

# Regular Expressions

Tokens can be described using regular expressions:

RE                                          | Token
--------------------------------------------|------
if                                          | if
[a-z][a-z0-9]*                              | ID
[0-9]+ ([0-9]+"."[0-9]*)\|([0-9]*"."[0-9]+) | NUM
("\-\-"[a-z]*"\n")\|(" "\|"\n"\|"\t")+      | REAL



# Regular Expression Notation

Notation | Meaning
---|---
a | An ordinary character stands for itself.
ε | The empty string.
M\|N | Alternation, choosing from M or N.
M·N | Concatenation, an M followed by an N.
MN  | Another way to write concatenation.
M*  | Repetition (zero or more times).
M+ | Repetition, one or more times.
M? | Optional, zero or one occurrence of M.
[a − zA − Z]  | Character set alternation.
.  |  A period stands for any single character except newline.
"a.+*" | Quotation, a string in quotes stands for itself literally.


# JavaCC Specification

```java
PARSER_BEGIN(MyParser)
   class MyParser {}
PARSER_END(MyParser)
/* For the regular expressions on the right, the token on the left will be returned: */
TOKEN : {
    < IF: "if" >
| < #DIGIT: ["0"-"9"] >
| < ID: ["a"-"z"] (["a"-"z"]|<DIGIT>)* >
| < NUM: (<DIGIT>)+ >
| < REAL: ( (<DIGIT>)+ "." (<DIGIT>)* ) |
( (<DIGIT>)* "." (<DIGIT>)+ )>
}
/* The regular expressions here will be skipped during lexical analysis: */
SKIP : {
<"--" (["a"-"z"])* ("\n" | "\r" | "\r\n")>
|"" | "\t" | "\n"
}
/* If we have a substring that does not match any of the regular expressions in TOKEN or SKIP, JavaCC will automatically throw an error. */
void Start() :
{}
{ (<IF>|<ID>|<NUM>|<REAL>)* }
```

* javacc -debug_parser scannerparser.jj
* javac *.java

Next, to input a string from the command prompt, run:

`java MyParser`

If you wish to run the tokenizer against a Java file, run it like this:

`java MyParser < program.java`
