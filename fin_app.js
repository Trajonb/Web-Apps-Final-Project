$(".comment-input button").on("click", function (event) { 
    $(".bg-modal").css("display", "flex");
}); 

$(".close").on("click", function (event) { 
    $(".bg-modal").css("display", "none");
}); 

$(".button2").on("click", function (event) { 
    var txtFile = "C:\subscribers.txt";
    var file = new File(txtFile); 
    const fs = require('fs');
    var input = $(".subfile input").val(); //get value of input and makes it >
    if (input == "") { //if the input box is empty
         window.alert("Empty!"); //displays window alert  notfying that >
    } else {
        file.open("w"); // open file with write access
        file.writeln(input);
        file.close();
    }
    $(".bg-modal").css("display", "none");

}); 


  