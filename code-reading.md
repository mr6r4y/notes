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

* OO programming has three hallmarks:
    * encapsulation
    * inheritance
    * polymorphism
* The OO programming paradigm encourages the distribution of functionality related code elements across the system
* Understanding of code frequently requires the understanding of code not in the same class
* Polymorphism and late binding make the dynamic behavior of the code hard to comprehend
* One must understand static and dynamic behaviour

### Delocalization

Soloway and Ehrlich (1984) introduced the concept of programming plan,
which is a generic fragment of code that represents typical scenarios in programming.
They observed that when a programming plan is distributed non-contiguously in a program,
it becomes hard to comprehend since only a part of the code is seen at a time and the reader
has to guess based on local information. They called this kind of plan delocalized.
This delocalized nature is pervasive in OO programming, and Dunsmore et al. (2001)
named the characteristic delocalization. Effective OO code reading
has to address this delocalization.

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

#### The Process

1. Read code line by line to build up a conceptual understanding of code fragments
1. Connect code fragments to form an overall picture
1. Compare with specifications to detect defects
1. Repeat until all code is abstracted and compared with specifications

### Abstraction-Driven Reading

* Many kinds of dependencies and couplings:
    * data dependencies
    * control dependencies
* Coupling metrics to measure and rank the classes and methods for determining reading order:
    * interaction coupling
    * component coupling
    * inheritance coupling
* Observe changes of state and outputs in terms of inputs and prior states
* Abstraction-driven reading is a systematic approach
* Encourages a deep understanding of the code
* Poor addressing of dynamic features of OOP

#### The Process

1. Determine the reading order
    1. Analyze the interdependencies and couplings within the whole object-oriented system. Read the classes with the least amount of dependencies first
    1. Analyze the methods within classes. Read the methods with the least amount of dependencies first
1. Read using abstraction
    1. For each method, reverse-engineer an abstract specification of the method. The method abstract specification may be used to compare with the class specification; it can also be used to support further reading and understanding of other methods (see tracing of referenced methods and classes below)
    1. Trace and understand all referenced classes during reading. This includes reading methods/classes, documentations, previously created abstractions, etc

## Code Readability Factors

* **Reader characteristics**: A reader’s experience and knowledge of programming, programming languages, and application domains play a significant role during code reading and comprehension
* **Intrinsic factors**: Similar to the intrinsic and accidental complexity of a design, code can have its own intrinsic and accidental complexity, which affects its readability. As we learned earlier, object-oriented programming makes delocalization more prevalent, and delocalized code is harder to read and understand
* **Representational factors**: Representation factors are broad and can include the programming language, whether the code has adequate and accurate comments, the complexity of the design, the naming conventions for variables and methods, etc
* **Typographic factors**: Typographic factors include font, color-coding of keywords or other programming entities, usage of white space and indentation, etc
* **Environmental factors**: Environmental factors are meant to contain anything else, e.g., the lighting in the reading spot, the integrated development environment (IDE), etc

### Simple Rules

* Pick a coding standard
* Add comments to the code and keep the comments up to date
* Choose your variables, function or method names, and other identifiers carefully and wisely
* Use simple programming structures - KISS principle
* Stay away from non-standard language featuress
* Logically group your code

## Artefacts to generate

* Control flow diagram (Call graph)
* Data flow diagram
* Cross-reference listing
* Structure chart
* Coupling metrics:
    * interaction coupling
    * component coupling
    * inheritance coupling

## Software Tools

## Mental Tools


## References

* [Code Reading Techniques](http://www.apress.com/la/book/9781484223451)

