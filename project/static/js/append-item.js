$(document).ready(function(){

  var appendItem =  
  "<tr>" +
    "<td><input id='id1' type='text' name='bill-ititle'></td>" +
    "<td><input id='id2' type='text' name='bill-amount'></td>" +
    " <td class='center'> <label> <input type='checkbox'  name='record'/>  <span><i class='fas fa-trash'></i></span> </label> </td>" +
  "</tr>"

  $('.item-btn-add').click(function(e){
    e.preventDefault();
    $(".add-bill table tbody").append(appendItem);
  })


  $('.item-btn-delete').click(function(e){
    e.preventDefault();
    $(".add-bill table tbody").find('input[name="record"]').each(function(){
      if($(this).is(":checked")){
            $(this).parents("tr").remove();
        }
    });
  })

  $(".bill-clear").click(function(e){
    e.preventDefault();
    $("table input").val(" ");
  })

  $(".bill-save").click(function(e){
    e.preventDefault();
  })
});

