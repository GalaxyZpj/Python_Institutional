function Call()
{ mob=txt.value; 
err=false
for(i=0;i<mob.length;i++)
{ c=mob.charCodeAt(i);
  if(!(c>=48 && c<=57))
  {err=true
  break;}
 }
if(err)
img.src='crs.png'
else
img.src='tick.png'
}