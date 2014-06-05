window.onload = pageLoad;

function pageLoad(){
	//$("ingadd").observe("click", ajaxAdd);

}

function ajaxAdd(){
	alert("stuiff");



}


function ingredientSubmit(){
	var ing = document.getElementById('ing');
	var amt = document.getElementById('amt');
	var type = document.getElementById('type');
	//alert(ing + amt + type);
	var node = document.createElement("li");
	var textnode = document.createTextNode(amt.value + " " + type.value + " " + ing.value);
	node.appendChild(textnode);
	document.getElementById('inglist').appendChild(node);
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
	node.appendChild(textnode);
	document.getElementById('instlist').appendChild(node);
	step.value = "";
}
