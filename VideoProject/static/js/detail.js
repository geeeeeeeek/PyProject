$(function () {

    function getCookie(name) {
        // Function to get any cookie available in the session.
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    function csrfSafeMethod(method) {
        // These HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    var page_title = $(document).attr("title");
    // This sets up every ajax call with proper headers.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // 点赞
    $("#like").click(function(){
      var id = $("#like").attr("video-id");
      $.ajax({
            url: '/video/like/',
            data: {
                video_id: id,
                'csrf_token': csrftoken
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                console.log(data)
                var likes = data.likes
                var user_liked = data.user_liked
                $('#like-count').text(likes)
                if(user_liked == 0){
                    $('#like').removeClass("grey").addClass("red")
                }else{
                    $('#like').removeClass("red").addClass("grey")
                }
            },
            error: function(data){
              alert("点赞失败")
            }
        });
    });

     // 收藏
    $("#star").click(function(){
      var id = $("#star").attr("video-id");
      $.ajax({
            url: '/video/collect/',
            data: {
                video_id: id,
                'csrf_token': csrftoken
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                console.log(data)
                var collects = data.collects
                var user_collected = data.user_collected
                $('#collect-count').text(collects)
                if(user_collected == 0){
                    $('#star').removeClass("grey").addClass("red")
                }else{
                    $('#star').removeClass("red").addClass("grey")
                }
            },
            error: function(data){
              alert("收藏失败")
            }
        });
    });

})





