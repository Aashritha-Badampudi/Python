"""2. Basic Syntax of for Loop
   ---------------------------

   * Syntax structure:
   -> for variable in sequence:
        statement

   * Role of loop variable:
   -> The loop variable is a temporary variable used by the for loop.
   -> Its role is:
        to store one item at a time from the sequence
        to change its value automatically in each iteration
        to represent the current element being processed
   -> Important points:
        The loop variable is created by the loop
        You do not manually change it
        Python assigns values to it automatically
        
   * Importance of indentation:
    -> Indentation is mandatory in Python.
    -> In a for loop:
        Indented statements belong to the loop
        Non-indented statements are outside the loop
    -> Why indentation is important:
        Python uses indentation to define blocks
        There are no {} brackets like in other languages
        Incorrect indentation causes errors or wrong logic
        Only indented lines are executed repeatedly

   * Flow of execution:
   -> The flow of execution of a for loop happens in this order:
        1️⃣ Python takes the first item from the sequence
        2️⃣ Assigns it to the loop variable
        3️⃣ Executes the indented statements
        4️⃣ Takes the next item
        5️⃣ Repeats the process
        6️⃣ Stops automatically when items are finished
   -> Key points:
        No condition checking by the programmer
        No manual increment needed
        Loop stops automatically
        """
