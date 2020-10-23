function output(num) {
	document.getElementById("screen").value+= num;
}

function solve() { 
    let x = document.getElementById("screen").value
    let y = eval(x) 
    document.getElementById("screen").value = y 
} 