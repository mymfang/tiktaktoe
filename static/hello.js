/*
document.addEventListener("DOMContentLoaded", function()
{
    document.querySelector("button").onclick = count;
});
*/

let x = 20;
alert(x);

function hello()
{
    document.querySelector("h1").innerHTML = "Hello!"
}

let counter = 0;

function count()
{
    counter++;
    document.querySelector("#counter").innerHTML = counter;
    if (counter == 10)
    {
        counter = 0;
    }
}