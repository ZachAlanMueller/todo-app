$(function() {
myArray = ["Feed dogs", "Do laundry", "Be productive"]
function clear(){
    document.getElementById("list").innerHTML = "";
    }
function write(){
    clear();
    for (i = 0; i < myArray.length; i++){
        document.getElementById("list").innerHTML += myArray[i];
        document.getElementById("list").innerHTML += "<br><br>";   
    }   
}

                
function clearElems() {
    myArray = [];
    write();
}
                
function removeTask() {
//alert('remove');
    var x = document.getElementById("toRemoveField").value;
    var found = ($.inArray(x, myArray) > -1);
    if (found) {
        var i = myArray.indexOf(x);
        myArray.splice(i, 1);                       
        document.getElementById("errors").innerHTML = "";    
    }
    else{
        document.getElementById("errors").innerHTML = "'" + x + "' entry found in your todo's!";             
    }
    write();                
}
                
function addTask() {
    //alert('add');
    var x = document.getElementById("toAddField").value;
    myArray.push(x);
    write();
    document.getElementById("toAddField").value = "";
}





write()
document.getElementById("clear").onclick = function() {clearElems()};           //Clear button
document.getElementById("toRemove").onclick = function() {removeTask()};        //Remove button
document.getElementById("toAdd").onclick = function() {addTask()};              //Add Button



                
});

