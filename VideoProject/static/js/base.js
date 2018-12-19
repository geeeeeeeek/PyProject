

$(function(){

    // 头像dropdown
    $('#v-header-avatar').dropdown();

    $('#v-search').bind('keypress',function(event){
        if(event.keyCode == "13")
        {
        	window.location = search_url + '?q='+$('#v-search').val();
        }
    });
});
