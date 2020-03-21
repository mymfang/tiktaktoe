document.addEventListener("DOMContentLoaded", function()
{
    document.querySelector("#countBtn").onclick = count;

    /*
    document.querySelector("#red").onclick = function()
    {
        document.querySelector("#hello").style.color = "red";
    }
    */

    document.querySelectorAll(".color-change").forEach(function(button)
    {
        button.onclick = function()
        {
            document.querySelector("#hello").style.color = button.dataset.color;
        }
    });

});


//let x = 20;
// alert(x);

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