window.toinsert = ""
function getSel(){
	var txtarea = document.getElementsByTagName("textarea")[0];
	var start = txtarea.selectionStart;
	var finish = txtarea.selectionEnd;
	var sel = txtarea.value.substring(start, finish);
	if (sel) {
		window.toinsert = txtarea.value.substring(0, start)
		window.toinsert2 = txtarea.value.substring(start, finish)
		window.toinsert3 = txtarea.value.substring(finish,txtarea.value.length+1 )
	} else if (toinsert) {
		var a = 0
	}
}

function subhead() {
	if (toinsert2.search("## ")!=-1) {
		toinsert2 = toinsert2.replace("## ","")
		document.getElementById('mta').value=toinsert+toinsert2+toinsert3
	} else {
		document.getElementById('mta').value=toinsert+"\n## "+toinsert2+toinsert3
		window.toinsert = ''
	}
}

function bold() {
	if (toinsert2.search("\\*\\*")!=-1) {
		toinsert2 = toinsert2.replace("**","")
		document.getElementById('mta').value=toinsert+toinsert2+toinsert3
	} else {
		document.getElementById('mta').value=toinsert+"**"+toinsert2+"**"+toinsert3
		window.toinsert = ''
	}
}

function italics() {
	if (toinsert2.search("\\*")!=-1) {
		toinsert2 = toinsert2.replace("*","")
		document.getElementById('mta').value=toinsert+toinsert2+toinsert3
	} else {
		window.before = "*"
		window.after = "*"
		document.getElementById('mta').value=toinsert+before+toinsert2+after+toinsert3
		window.toinsert = ''
	}
}

function bullet() {
		document.getElementById('mta').value=toinsert+"\n * "+toinsert2.replace(/\n/g,"\n * ")+toinsert3
		window.toinsert = ''
}

function sup() {
	if (toinsert2.search("~")!=-1) {
		toinsert2 = toinsert2.replace("~","")
		document.getElementById('mta').value=toinsert+toinsert2+toinsert3
	} else {
		document.getElementById('mta').value=toinsert+"~"+toinsert2+"~"+toinsert3
		window.toinsert = ''
	}
}

function link() {
	urlget = prompt("Please enter a URL:","http://modding.ssblur.com")
	if (urlget==null) {
		urlget = "http://modding.ssblur.com"
	}
	window.before = "[";
	window.after = "]("+urlget+")";
	document.getElementById('mta').value=toinsert+before+toinsert2+after+toinsert3
	window.toinsert=''
}

function head() {
	if (toinsert2.search("# ")!=-1) {
		toinsert2 = toinsert2.replace("# ","")
		document.getElementById('mta').value=toinsert+toinsert2+toinsert3
	} else {
		document.getElementById('mta').value=toinsert+"\n# "+toinsert2+toinsert3
		window.toinsert = ''
	}
}
window.onload = window.setInterval(function(){getSel()}, .3)