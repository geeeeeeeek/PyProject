
// 删除
$(".video-list").on("click", ".video-delete", function () {
  var tr = $(this).closest("tr");
  var id = $(tr).attr("video-id"); 
    $('.ui.tiny.modal.delete')
    .modal({
      closable  : true,
      onDeny    : function(){ 
        return true;
      },
      onApprove : function() { 

        $.ajax({
            url: '/messages/send-message/',
            data: {},
            cache: false,
            type: 'POST',
            success: function (data) {
                 
            },
            error: function(data){
              alert("error"+id)
            }
        });

      }
    })
    .modal('show'); 
});

// 编辑
$(".video-list").on("click", ".video-edit", function () {
  var tr = $(this).closest("tr");
  var id = $(tr).attr("video-id"); 
    $('.ui.tiny.modal.edit')
    .modal({
      closable  : true
    })
    .modal('show'); 
});