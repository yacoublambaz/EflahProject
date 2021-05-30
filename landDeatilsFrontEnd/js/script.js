
function radioChange(){
    if (document.getElementById('exampleRadios1').checked) {
        document.getElementById("landOwner").style.display="block";
        document.getElementById("landUser").style.display="none";
    }
    
    else if (document.getElementById('exampleRadios2').checked) {
        document.getElementById("landOwner").style.display="none";
        document.getElementById("landUser").style.display="block";
    }
}