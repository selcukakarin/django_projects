AJAX İSTEĞİ
var token = '{{ csrf_token }}'; // add to top in js code
$.ajax({
        type: 'POST',
        headers: {
          "X-CSRFToken": token
        },
        url: `editableTableChange_${tablo_id}/${row_uuid}/`,
        data: {
          "editable_column_name": `${changed_col}`,
          "editable_changed_value": $(this).text()
        },
        });

URL

path('editableTableChange_Cari/<uuid:uuid>/', guncelleView.editableTableChange_Cari, name="editableTableChange_Cari"),
path('cari_adres/editableTableChange_CariAdres/<uuid:uuid>/', guncelleView.editableTableChange_CariAdres, name="editableTableChange_CariAdres"),
path('cari_erisim/editableTableChange_CariErisim/<uuid:uuid>/', guncelleView.editableTableChange_CariErisim, name="editableTableChange_CariErisim"),

VİEW

@login_required(login_url="Kullanici:kullanici_giris")
def editableTableChange_Cari(request,uuid):

    col_nm=request.POST.get("editable_column_name")
    chg_val=request.POST.get("editable_changed_value")
    print("COLUMNS NAMES EDITABLE")
    print(str(col_nm))
    print("EDITABLE CHANGED VALUE")
    print(chg_val)
    obj = Cari.objects.get(id=uuid)
    setattr(obj , col_nm, chg_val)
    obj.save()
    #MyModel.objects.filter(pk=some_value).update(field1='some value')

    #messages.info(request, "\'" + cari_verisi.unvan + "\'" + "{}".format(_(": Koduna Sahip Değer Güncellendi")))
    return redirect("Cari:cari")


JS

$('#DataTables_Table_1').on('focusout', ' td', function(event) 
        {
        event.preventDefault();
        var currentRow = (this).closest('tr');

        var cols_dt = $('#DataTables_Table_1').DataTable().settings().init().columns;
        var row_uuid = $('#DataTables_Table_1').DataTable().row(currentRow).data()["id"];
        var colIndex = $('#DataTables_Table_1').DataTable().cell(this).index().column;
        var changed_col = cols_dt[colIndex].data;
        if ($(this).has("a").length == 1) {
          $(this).find('a')
            .attr('contenteditable', 'false')
        } else {
          $(currentRow).find('td')
            .attr('contenteditable', 'false')
        }
        $(currentRow).find('td')

          .css('background', "");
        $(this).css('padding', '.75rem 1.25rem ');

        console.log(changed_col)
        console.log($(this).text())
        console.log(row_uuid)


        $.ajax({
        type: 'POST',
        headers: {
          "X-CSRFToken": token
        },
        url: `editableTableChange_${tablo_id}/${row_uuid}/`,
        data: {
          "editable_column_name": `${changed_col}`,
          "editable_changed_value": $(this).text()
        },
        });
        })
        //--->save single field data > end

          $("#DataTables_Table_1").on('dblclick', 'td', function (e) {

            var currentRow = (this).closest('tr');
            var row_uuid = $('#DataTables_Table_1').DataTable().row(currentRow).data();

            
            if ($(this).hasClass("select-checkbox")) {

            } else {
              $(currentRow).find('td')
              .css('background', "#d2cbc0");
            $(this).css('padding', '.75rem 1.5rem');
            console.log(this)
              if ($(this).has("a").length == 1) {
                $(this).find('a')
                  .attr('contenteditable', 'true')
                $(this).find('a').focus();
              } else {
                $(currentRow).find('td')
                  .attr('contenteditable', 'true')
                $(this).focus();
              }
            }


          });



        // DegerleriGetir - end
      };
      