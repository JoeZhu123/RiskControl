//js get today's date
function time()
{
   var day_choice=document.getElementById("subject");
   console.log(day_choice.value);
   var now=new Date();
   var year=now.getFullYear();
   var month=now.getMonth();
   var date=now.getDate();
   //write into html
   for(var i=0;i<day_choice.value;i++)
   {
       document.getElementById("day_now"+i.toString()).innerHTML=year+"/"+(month+1)+"/"+(date-i);
   }
}
