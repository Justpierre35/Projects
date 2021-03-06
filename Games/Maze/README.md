<strong>roboc' Project</strong>

Exercice as part of the Openclassrooms "Learn to program in Python" (end of Chapter III).

https://openclassrooms.com/courses/apprenez-a-programmer-en-python

--

<b>INSTRUCTIONS :</b>

<p>Your mission is to design and <strong>develop a little game to control a robot in a maze</strong>.This game should be developed in console for accessibility reasons. I called it ... <em>Roboc</em>.</p>

<p>The game is a maze made up of <strong>obstacles</strong> : wall are simply there to slow down, doors that can be crossed and at least one point through which you can leave the labyrinth. If the robot reaches this point, the game is considered to have been won.</p>

 

<h3>robot control</h3>
<p>The robot is moveable by commands entered on the keyboard. The following commands are :</p>
<ui>
<li><em>Q</em> which should allow you to save and exit the game in progress ;</li>
<li><em>N</em> which instrucs the robot to <strong>move north</strong> ;</li>
<li><em>E</em> which instrucs the robot to <strong>move east</strong> ;</li>
<li><em>S</em> which instrucs the robot to <strong>move south</strong> ;</li>
<li><em>O</em> which instrucs the robot to <strong>move west</strong> ;</li>
<li>Each of the directions above who followed a number makes it possible to advance by several boxes (for example 3E to advance by three boxes towards the east).</li>
</ui>
<p>&nbsp;</p>
<h3>Maze display</h3>
<p>The maze is seen from above. A symbol represents an obstacle or your own robot. You can refer to the example to get more information.</p> <p>To recognize the nature of the obstaclesm one must obviously represent each obstacle by a <strong>different symbol</strong>. Otherwise, it will be difficult to differentiate the walls of exit doors.</p>
<p>&nbsp;</p>

<h3>Games features</h3>
<p>The game must :</p>
<ul>
 <li><strong>Automatically save</strong> each game for each move to allow them to continue later ;</li>
 <li><strong>Offer several maps</strong> that are easy to edit. Each of the available maps will be in a file with the extention <em>txt</em> in a particular folder. It will therefore be easy to add, delete or modify maps.</li>
 </ul>
 <p>&nbsp;</p>
<ul>
<h3>At the launch of the program</h3>
<p>The first thing to do is to find the existing maps, kept in our <em>txt</em> files, to load them and to check that a game was not in progress. If a game is in progress, <strong>offer to continue this game</strong> (see the below example).</p>
<p>Choosing a map start the game. The same thing happens if you ask to play an already existing game. On each turn, the maze is displayed with the position of each obstacle and the position of the robot.</p>
</ul>
<p>&nbsp;</p>
<h3>Return examples</h3>
<p>Below you can find out what we could see when running the program. Note that :</p>
<ul>
<li>The symbols used are O for a wall, . for a door, U for the exit and X for the robot itself ;</li>
<li>The robot cannot pass through walls ;</li>
<li>The example below in an example of the easy card : <em>facile</em>.</li>
</ul>
<pre>python roboc.py<br>

Existing mazes :
  1 - facile.
  2 - prison.

Enter a number to select the maze : 1

OOOOOOOOOO
O O    O O
O . OO   O
O O O   XO
O OOOO O.O
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO


> s

OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO OXO
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO


> n

OOOOOOOOOO
O O    O O
O . OO   O
O O O   XO
O OOOO O.O
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO


> 2s

OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO OXO
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO


OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO O.O
O O O   XU
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO


> e

OOOOOOOOOO
O O    O O
O . OO   O
O O O    O
O OOOO O.O
O O O    X
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO


That's the way out


You win !!!
</pre>
