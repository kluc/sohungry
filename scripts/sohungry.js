window.onload = pageLoad;

function pageLoad(){
	//$("ingadd").observe("click", ajaxAdd);

}

function ajaxAdd(){
	alert("stuiff");



}

function deleteCheckedItems(){
	$('input:checkbox.delete').each(function(){
		if(this.checked){
			$(this).parent().remove();
		}
	});
}


function ingredientSubmit(){
	var ing = document.getElementById('ing');
	var amt = document.getElementById('amt');
	var type = document.getElementById('type');
	//alert(ing + amt + type);
	
	
	
	var node = document.createElement("li");
	var textnode = document.createTextNode(amt.value + " " + type.value + " " + ing.value);
	document.getElementById('inglist').appendChild(node);
	
	
	var d = document.createElement("input");
	d.className = "delete";
	d.setAttribute("type", "checkbox");
	//document.getElementById('inglist').appendChild(node);
	node.appendChild(d);
	node.appendChild(textnode);
	ing.value = "";
	amt.value = "";
	$('type option').prop('selected', function(){
		return this.defaultSelected;
	});
}

function instructionSubmit(){
	var step = document.getElementById('step');
	var node = document.createElement("li");
	var textnode = document.createTextNode(step.value);
	var d = document.createElement("input");
	d.className = "delete";
	d.setAttribute("type", "checkbox");
	node.appendChild(d);
	node.appendChild(textnode);

	document.getElementById('instlist').appendChild(node);
	
	step.value = "";
}
