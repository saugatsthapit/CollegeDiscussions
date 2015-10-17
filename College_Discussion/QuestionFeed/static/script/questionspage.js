$(document).ready(function(){
	$('#askquestionpopup').dialog({ 
		autoOpen:false, 
		resizable:false,
		draggable:false,
		height: 480,
		width: 560,
		modal:true, 
		title:"Ask Question",
		// buttons:[{ text:"ASK", click : function(){
//  			$(this).dialog("close");}
//  		},
//  		 {text: "CANCEL" , click : function(){
//  			$(this).dialog("close");}
// 		}]
	});
	// $('#askquestionpopup:eq(0)').dialog("widget").find(".ui-dialog-titlebar").css({opacity:0%, border:0});
	$('#askquestion').click(function(){
		$('#askquestionpopup').dialog("open")
	});
	
	$('#canceldialog').click(function(){
		$('#askquestionpopup').dialog("close")
	});
	
	
});
