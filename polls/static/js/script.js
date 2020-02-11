$( document ).ready(function() {
    console.log( "ready!" );

   var filters = document.getElementById("filters").value;
   console.log(filters);
   var type = document.getElementById("one").value;
   console.log(type);

   $.ajax({
        url: '../ajax/tcs_list/',
        type: 'GET',
        data: {"filters":filters,"one":type},
        success: function(data) {
            console.log("Sus");
        if (data.work){
            console.log("Deu certo");

        }else{
            console.log("Deu errado");
        }


	    },
	    erro: function(){
	       console.log("Deu pau");

	    }

});

});