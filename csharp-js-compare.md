# C# and JavaScript

Learning your first programming language is hard. It's hard because you're not only learning a language, but you're also learning _how to program_.

It is often said that learning a second programming language is easier because you now have the mental model of programming and how programming languages work. Now you can transfer the knowledge from the language you know to the language you're learning.

---

<div style="display: grid; grid-template-columns: auto auto auto; grid-gap: 8px;">

<div style="font-weight: bold"> </div>
<div style="font-weight: bold"> C# </div>
<div style="font-weight: bold"> javascript </div>

<div> if statement </div>

<div class="highlight highlight-source-cs">
<pre>
int numHats = 50;
if (numHats > 10)
{
    Console.WriteLine("Why do you have so many hats?");
g}
else if (numHats <= 10 && numHats >= 2)
{
    Console.WriteLine("You have a reasonable number of hats.");
}
else
{
    Console.WriteLine("You need more hats!");
}
</pre>
</div>

<div class="highlight highlight-source-js">
<pre>
const numHats = 50;
if (numHats > 10) {
    console.log("Why do you have so many hats?");
} else if (numHats <= 10 && numHats >= 2) {
    console.log("You have a reasonable number of hats.");
} else {
    console.log("You need more hats!");
}
</pre>
</div>

<div> for loop </div>
<div class="highlight highlight-source-cs">
<pre>
for (int i=0; i&lt;20; ++)
{
    Console.WriteLine($"The number is {i}");
}
</pre>
</div>
<div class="highlight highlight-source-js">
<pre>
for (let i=0; i&lt;20; ++) {
    console.log(`The number is ${i}`);
}
</pre>
</div>

<div> foreach loop </div>
<div class="highlight highlight-source-cs">
<pre>
List&lt;string&gt; foods = new List&lt;string&gt;()
{
    "Brussels Sprout", "Toast", "Steak", "Tomato"
};
foreach (string food in foods)
{
    Console.WriteLine($"You can eat {food}.");
}
</pre>
</div>
<div class="highlight highlight-source-js">
<pre>
const foods = ["Brussels Sprout", "Toast", "Steak", "Tomato"];
for (let food of foods) {
    console.log(`You can eat ${food}.`);
}
</pre>
</div>

</div>
