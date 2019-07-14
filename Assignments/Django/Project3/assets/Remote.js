function call() {
    if(txt.value.length >4) {
        result.innerHTML = "<font color = 'red'>ONLY 4 DIGITS ALLOWED</font>"
    }
    else {
        result.innerHTML = ""
    }
}
function cellHighlight(){
    s = txt.value[txt.value.length - 1]
    console.log(s)
    switch(s) {
        case "1":
            one.style.backgroundColor = "green"
            setTimeout(function() { one.style.backgroundColor = "white"}, 80);
            break;
        case "2":
            two.style.backgroundColor = "green"
            setTimeout(function() { two.style.backgroundColor = "white"}, 80);
            break;
        case "3":
            three.style.backgroundColor = "green"
            setTimeout(function() { three.style.backgroundColor = "white"}, 80);
            break;
        case "4":
            four.style.backgroundColor = "green"
            setTimeout(function() { four.style.backgroundColor = "white"}, 80);
            break;
        case "5":
            five.style.backgroundColor = "green"
            setTimeout(function() { five.style.backgroundColor = "white"}, 80);
            break;
        case "6":
            six.style.backgroundColor = "green"
            setTimeout(function() { six.style.backgroundColor = "white"}, 80);
            break;
        case "7":
            seven.style.backgroundColor = "green"
            setTimeout(function() { seven.style.backgroundColor = "white"}, 80);
            break;
        case "8":
            eight.style.backgroundColor = "green"
            setTimeout(function() { eight.style.backgroundColor = "white"}, 80);
            break;
        case "9":
            nine.style.backgroundColor = "green"
            setTimeout(function() { nine.style.backgroundColor = "white"}, 80);
            break;
        case "0":
            zero.style.backgroundColor = "green"
            setTimeout(function() { zero.style.backgroundColor = "white"}, 80);
            break;
    }
}