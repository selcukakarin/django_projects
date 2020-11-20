typeDropDown.onchange=function(){
  $('#columnId')
    .find('option')
    .remove()
  $.ajax({
          url: "{% url 'Columns_definition:fillToField' %}", //'http://127.0.0.1:8888/en-gb/Referans/test/kolon',
          type: 'GET',
          dataType: 'json',
          async: false,
          data: { 
            tblTypeId: typeDropDown.options[typeDropDown.selectedIndex].value, 
          },
          error: function () {
          },
          success: function (res) {
            console.log("merhaba")
            for(var i=0;i<=res.length-1;i++){ 
              var opt = document.createElement('option');
              opt.value = res[i];
              opt.innerHTML = res[i];
              columnId.appendChild(opt);
            }
          }
        });
}