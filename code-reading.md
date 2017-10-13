# Code Reading

## Strategies for Code Reading

### Oppurtunistic reading

* Running code with test data is not enough to build a mental image of the code base
* To read and understand the code, one has to build layered abstractions of the code
* Code reading is hard and time-consuming
* "As-needed" (opportunistic) reading approach usually adopted
* Avoidance of deep-understanding is energy saving
* Focus on local program behavior in this approach
* Failure to construct successful modifications to the program
* Failure to detect critical interactions among program components

### Top-down reading

* Similar to how we write code
* Follow a divide and conquer approach to decompose a high-level function into multiple low-level ones
* Appreciate the overall purpose first, then follow by understanding implementation
* Forming hypotheses about the code, whcih are subsequently verified, modified or rejected
* Scan the code for searching familiar clues in the text (beacons, program plans)
* Better approach when the overall programming purpose is known
* Better for reading well-documented code

### Bottom-up reading

* Opposite of top-down reading
* Understand small fragments of code, then combine chunks to understand larger portions of the program
* Deep knowledge of programming language and constructs is needed
* Deep knowledge of the application domain is needed
* Identify and understand control flow and data flow greatly facilitates global program comprehension
* Cross-referencing the program domain and the application domain tends
to confirm and enhance the level of understanding
* Reader’s experience and knowledge play significant role during reading and comprehension


## OOP Challenges

## Techniques

### Reading by Stepwise Abstraction

* A bottom-up reading technique
* "Program writing is expanding the known function into a program and program reading is abstracting the known program into a function"
* When reading code for defect detection, one compares the known functions (design) to their expansions (code)
* Recognize directly what the code does or mentally transform it into something that can be recognized directly
* Structured program of any size can be read and understood in a completely systematic manner by reading and understanding its hierarchy of prime programs and their abstractions
* A prime program is a fragment of code that has one entry and one exit and is irreducible in some sense
* A well-structured and documented program can be read top-down
* For poorly structured and documented code - bottom-up reading is a better strategy
* Bottom-up reading allows one to discover the intermediate abstractions, successively at higher levels
* The process of bottom-up reading is called stepwise abstraction

1. Read code line by line to build up a conceptual understanding of code fragments
1. Connect code fragments to form an overall picture
1. Compare with specifications to detect defects
1. Repeat until all code is abstracted and compared with specifications

### Abstraction-Driven Reading

### Use-Case-Driven Reading

## Code Readability Factors

## Artefacts to generate

* Control flow diagram (Call graph)
* Data flow diagram
* Cross-referencing

## Software Tools

## Mental Tools


## References


chain of actions

