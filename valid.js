function check(){
    var a=document.getElementById("first_name").value;
    var b=document.getElementById("middle_name").value;
    var c=document.getElementById("last_name").value;
    var d=document.getElementById("email").value;
    var e=document.getElementById("car_number").value;

    var l=/^[A-Za-z]+$/;
    var i,x,y,z;
    if(a=="" || b=="" || c=="")
    {
        window.alert("Name should not be blank !!");
        return false;
    }
    if(a.match(l)==null || b.match(l)==null || c.match(l)==null)
    {
        window.alert("Name must be in letters only !!");
        return false;
    }
    if(!(d.length==23 && Number.isInteger(Number(d.slice(0,2))) && Number.isInteger(Number(d.slice(5,8))) && d.slice(2,5).match(l) && d.slice(8,d.length).match("@nirmauni.ac.in")))
    {
        window.alert("Invalid Email Id !! Email must in format- DDCCCDDD@nirmauni.ac.in");
        return false;
    }
    if(!(e.length==10 && Number.isInteger(Number(e.slice(2,4))) && Number.isInteger(Number(e.slice(6,10))) && e.slice(0,2).match(l) && e.slice(4,6).match(l) ))
    {
        window.alert("Invalid Number !! Car Number in format- XY05AB0000");
        return false;
    } 

    window.alert("Successfully Submitted :)")
    return true;
}

