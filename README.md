## Тестовое Задание
> Ulybin, Dima <Dima.Ulybin@Dell.com>

> Санкт-Петербург 2017


You have 100 lamps in array [1,2,3,4,5…..99,100]
And we have 100 trained frogs.

Each frog jumps on a lamp and turns its each switch on/off, in this order:
```
1.       First frog just on each lamp
2.       Second frog jump directly to the second lamp and then to the 4th lamp, 6th , 8th …
3.       Third frog jump directly to the third lamp and then to the 6th lamp, 9th , 12th …
4.       Forth frog jump directly to the forth lamp and then to the 8th lamp, 12th , 16th …
…
100.  The 100th frog jump directly to the 100 lamp and then gets out
```
Our Framework already supplied the function that presses the lamp in the correct index: press(i)
Please write an algorithm or code that will imitate the jumping frogs, using the given function prees(i).
