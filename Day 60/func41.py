"""The concept of scope:
   --------------------

-> What is scope exactly?
   The scope is nothing but where a variable can be used.

🏠 House Example
Kitchen items → only in kitchen
Bedroom items → only in bedroom
TV in hall → everyone can use

-> Variables also work like this.
Some variables are only inside a function.
Some are available everywhere.

1️⃣ Local scope(Most imp):
  A variable created inside a function is called as local scope.
  It can be used only inside the function.

2️⃣ Global scope
  A variable which is created outside of all the functions is known as global scope.
  It can be used anywhere in the program.

3️⃣ Why We Need Global Keyword?
  If you want to change a global variable inside function:
  Use global

4️⃣ Nested Scope
  A function inside a function is known as nested scope.

5️⃣ LEGB Rule
  It is the rule that python follows to find a variable.
  The obbreviation of LEGB is:
    L -> Local 
    E -> Enclosing
    G -> Global
    B -> Built-in
  When we use a variable name, python checks one by one in this order. The moment it finds the variable, it stops searching.
  Now let us see each of them in detail:
  1️⃣ L - Local Scope
   A variable created inside the function. It belongs only to that function.
   Local variables:
    Are created when function runs
    Are destroyed when function finishes
    They are temporary.
  2️⃣ E - Enclosing Scope
    A variable in the outer function, when you have a function inside another function.
    This is also called nested function scope.
    Here:
     x is not local to inner()
     It belongs to outer()
     So it's called Enclosing scope
    To modify it:
      If you want to change it inside inner function:
      You must use "nonlocal"
  3️⃣ G - Global Scope
    A variable which is created outside the function is known as global variable or global scope. I can be accessed anywhere in the program.
    If you want to modify the global variable we use the "global" keyword inside a function.

  4️⃣ B - Built-in Scope
    It contains python's default functions and keywords. Eg: print(), len(), int(), etc
   🔹 Example
      print(len("Hello"))
      len() is built-in.
      If Python doesn’t find a variable in:
      Local → Enclosing → Global
      It checks Built-in last.

🎯 Visual Memory Trick
 ___________
|  Local    |
|    ↓      |
| Enclosing |
|    ↓      |
| Global    |
|    ↓      |
| Built-in  |
|___________|

    """ 