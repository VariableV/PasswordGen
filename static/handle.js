// author: Maheen Hussain
$(document).ready(function(){
	$("#textOne").change(function(){
		$.ajax({
			data : {
				webname : $("#textOne").val()
			},
			type : "POST",
			url : "/genpw"
		}).done(function(data){
			var txt = data.retn;
			var outbox = document.getElementById("textTwo");
			var previousinterval=0;
			var finised=true;
			if (outbox.value.length > 0){
				finised=false;
				// clear it
				var str=outbox.value;
				function removeText(){
					if(str.length!=0){
						str = str.substring(0,str.length-1);
						outbox.value=str;
						previousinterval = setTimeout(removeText, 50);
					}
					else{
						finised=true;
					}
				}
				removeText();
			}
			var i = 0;
			var speed = 50;
			function typeWriter(){
				if (i < txt.length){
					if(finised){
						outbox.value += txt.charAt(i);
						i++;
					}
					setTimeout(typeWriter, speed);	
				}	
			}
			typeWriter();
		});
	});
});