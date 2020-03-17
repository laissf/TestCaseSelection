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
            preeencher_fillin("tcin",data.tcs_in);
            preeencher_fillout("tcout",data.tc_out);
        }else{
            console.log("Deu errado");
        }

	    },
	    erro: function(){
	       console.log("Deu pau");
	    }

});

});


function preeencher_fillin(id, tcs){
    var div = document.getElementById(id);

    for (tc of tcs){
        var p = document.createElement("p");
        var label = document.createElement("label");
        var input = document.createElement("input");
        var span = document.createElement("span");

        input.type ="checkbox";
        input.id   = tc["key"];
        input.classList.add("filled-in");
        input.checked = true;
        label.textContent = tc["key"] + " : "+ tc["title"];
        label.setAttribute("for", tc["key"]);
        p.appendChild(input);
        p.appendChild(label);
        div.appendChild(p);
    }
}


function preeencher_fillout(id, tcs){
    var div = document.getElementById(id);

    for (tc of tcs){
        var p = document.createElement("p");
        var label = document.createElement("label");
        var input = document.createElement("input");
        var span = document.createElement("span");

        input.type ="checkbox";
        input.id   = tc["key"];
        input.classList.add("filled-in");
        label.textContent = tc["key"] + " : "+ tc["title"];
        label.setAttribute("for", tc["key"]);
        p.appendChild(input);
        p.appendChild(label);
        div.appendChild(p);
    }
}