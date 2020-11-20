$(document).ready(function () {
    let _hesapKodu = $('#hesapKodu')
    let _unvan = $('#unvan')
    let _ad = $('#ad')
    let _soyad = $('#soyad')
    let _aktifPasif = $('#aktifPasif')
    let _field1 = $('#field1')
    let _field2 = $('#field2')
    let _field3 = $('#field3')
    let _field4 = $('#field4')
    let _field5 = $('#field5')
    let _field6 = $('#field6')
    let _field7 = $('#field7')
    let _field8 = $('#field8')
    let _resim = $('#resim')
    let _field10 = $('#field10')
    let _field11 = $('#field11')
    let _field12 = $('#field12')
    let _field13 = $('#field13')
    let _field14 = $('#field14')
    let _field15 = $('#field15')
    let _field16 = $('#field16')
    let _field17 = $('#field17')
    let _field18 = $('#field18')
    let _field19 = $('#field19')
    let _field20 = $('#field20')
    let _field21 = $('#field21')
    let _field22 = $('#field22')
    let _field23 = $('#field23')
    let _field24 = $('#field24')
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
    function beforeAjax(csrftoken) {
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    }
    
    /*    FOR MODAL    */
    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
    /*    FOR MODAL    */

    /*    FOR DATATABLE    */
    let currentData;
    let data_delete_ids = [];
    let rowCountSorted = [5, 10, 25, 50, 100].sort(function (a, b) {
        return a - b;
    })
    let table = $('#datatables').DataTable({
        colReorder: true,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": '/customers/drawDt',
            "type": "GET"
        },
        "language": {
            "sDecimal": ",",
            "sEmptyTable": "Tabloda herhangi bir veri mevcut değil",
            "sInfo": "_TOTAL_ kayıttan _START_ - _END_ arasındaki kayıtlar gösteriliyor",
            "sInfoEmpty": "Kayıt yok",
            "sInfoFiltered": "(_MAX_ kayıt içerisinden bulunan)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "<span>Kayıt:</span> _MENU_ ",
            "sLoadingRecords": "Yükleniyor...",
            "sProcessing": "İşleniyor...",
            "sSearch": "<span>Arama Anahtarı:</span>",
            "sZeroRecords": "Eşleşen kayıt bulunamadı",
            "oPaginate": {
                "sFirst": "İlk",
                "sLast": "Son",
                "sNext": "Sonraki",
                "sPrevious": "Önceki"
            },
            "oAria": {
                "sSortAscending": ": artan sütun sıralamasını aktifleştir",
                "sSortDescending": ": azalan sütun sıralamasını aktifleştir"
            },
            "select": {
                "rows": {
                    "_": "%d kayıt seçildi",
                    "0": "",
                    "1": "1 kayıt seçildi"
                }
            }
        },
        "lengthMenu": rowCountSorted,
        "pageLength": rowCount,
        "dom": "lfBrtip",
        // "columnDefs":
        //         [
        //           {
        //             "visible": false,
        //             "targets": 1,
        //           }
        //         ],
        "select": {
            "style": 'multi',
            "selector": 'tr'
        },
        "columns": [
            {
                "data": "id"
            },
            {
                "data": "hesapKodu"
            },
            {
                "data": "unvan"
            },
            {
                "data": "ad"
            },
            {
                "data": "soyad"
            },
            {
                "data": "aktifPasif"
            },
            {
                "data": "field1"
            },
            {
                "data": "field2"
            },
            {
                "data": "field3"
            },
            {
                "data": "field4"
            },
            {
                "data": "field5"
            },
            {
                "data": "field6"
            },
            {
                "data": "field7"
            },
            {
                "data": "field8"
            },
            {
                "data": "resim"
            },
            {
                "data": "field10"
            },
            {
                "data": "field11"
            },
            {
                "data": "field12"
            },
            {
                "data": "field13"
            },
            {
                "data": "field14"
            },
            {
                "data": "field15"
            },
            {
                "data": "field16"
            },
            {
                "data": "field17"
            },
            {
                "data": "field18"
            },
            {
                "data": "field19"
            },
            {
                "data": "field20"
            },
            {
                "data": "field21"
            },
            {
                "data": "field22"
            },
            {
                "data": "field23"
            },
            {
                "data": "field24"
            },
            // {
            //     "data": null,
            //     "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
            //     '<button type="button" class="btn btn-danger">Delete</button>'
            // }
        ],
        "buttons": [{
                "id": 'myBtn',
                "type": 'button',
                "className": 'dynamicCreateBtn btn btn-secondary',
                "text": 'create',
                "titleAttr": 'Olustur',
                enabled: false,
                action: function (e, dt, node, config) {
                    //This will send the page to the location specified                                                  	
                    console.log("create")
                    modal.style.display = "block";
                }
            },
            {

                "className": 'dynamicUpdateBtn btn btn-secondary',
                "text": 'update',
                "titleAttr": 'Güncelle',
                enabled: false,
                action: function (e, dt, node, config) {
                    console.log("update ")
                    console.log(currentData)
                }
            },
            {
                "className": 'dynamicDeleteBtn btn btn-secondary',
                "text": 'delete',
                "titleAttr": 'Sil',
                enabled: false,
                action: function (e, dt, node, config) {
                    console.log("delete")
                    console.log("delete_list : " + data_delete_ids)
                    delete_list_element(delete_email_url, data_delete_ids)
                    data_delete_ids = [];
                }
            }
        ],
    });
    dtBtnChkList()

    function dtBtnChkList() {
        if (table.rows({
                selected: true
            }).count() === 0) {
            table.buttons(['.dynamicCreateBtn']).enable(true);
            table.buttons(['.dynamicDeleteBtn']).enable(false);
            table.buttons(['.dynamicUpdateBtn']).enable(false);
        } else if (table.rows({
                selected: true
            }).count() === 1) {
            table.buttons(['.dynamicCreateBtn']).enable(true);
            table.buttons(['.dynamicDeleteBtn']).enable(true);
            table.buttons(['.dynamicUpdateBtn']).enable(true);
        } else if (table.rows({
                selected: true
            }).count() > 1) {
            table.buttons(['.dynamicCreateBtn']).enable(true);
            table.buttons(['.dynamicDeleteBtn']).enable(true);
            table.buttons(['.dynamicUpdateBtn']).enable(false);
        }

    };
    //--->Seçilen satırların silinmesi için listeye ekleme ve çıkarma işlemi
    table
        .on('select', function (e, dt, type, indexes) {
            console.log("select")
            dtBtnChkList()
            currentData = Object.values(table.rows(indexes).data())[0].id
            data_delete_ids.push(String(currentData));
        })
        .on('deselect', function (e, dt, type, indexes) {
            console.log("deselect")
            dtBtnChkList()
            currentData = Object.values(table.rows(indexes).data())[0].id
            data_delete_ids.splice(data_delete_ids.indexOf(currentData), 1);
        });

        /*    FOR SUBMIT    */
    
        $('#customer_form').on('submit', function (event) {
            event.preventDefault();
            let create_data = {
                hesapKodu: _hesapKodu.val(),
                unvan: _unvan.val(),
                ad: _ad.val(),
                soyad: _soyad.val(),
                aktifPasif: _aktifPasif.val(),
                field1: _field1.val(),
                field2: _field2.val(),
                field3: _field3.val(),
                field4: _field4.val(),
                field5: _field5.val(),
                field6: _field6.val(),
                field7: _field7.val(),
                field8: _field8.val(),
                resim: _resim.val(),
                field10: _field10.val(),
                field11: _field11.val(),
                field12: _field12.val(),
                field13: _field13.val(),
                field14: _field14.val(),
                field15: _field15.val(),
                field16: _field16.is(':checked'),
                field17: _field17.is(':checked'),
                field18: _field18.val(),
                field19: _field19.is(':checked'),
                field20: _field20.val(),
                field21: _field21.val(),
                field22: _field22.val(),
                field23: _field23.val(),
                field24: _field24.val()
            };
            create_ajax_method(create_data);
        });
    
        function create_ajax_method(create_data) {
            beforeAjax($("#customer_form > [name=csrfmiddlewaretoken]").val());
            $.ajax({
                url: create_url, // the endpoint
                type: "POST", // http method
                data: create_data, // data sent with the post request
    
                // handle a successful response
                success: function (json) {
                    //$('#post-text').val(''); // remove the value from the input
                    console.log(json); // log the returned json to the console
                    console.log("ajax success"); // another sanity check
    
                    if (json.error) {
                        alert(json.result);
                    } else {
                        table.row.add( [
                            json.id,
                            json.hesapKodu,
                            json.unvan,
                            json.ad,
                            json.soyad,
                            json.aktifPasif,
                            json.field1,
                            json.field2, 
                            json.field3, 
                            json.field4,
                            json.field5, 
                            json.field6 ,
                            json.field7,
                            json.field8,
                            json.resim,
                            json.field10,
                            json.field11,
                            json.field12,
                            json.field13,
                            json.field14,
                            json.field15,
                            json.field16,
                            json.field17,
                            json.field18,
                            json.field19,
                            json.field20,
                            json.field21,
                            json.field22,
                            json.field23,
                            json.field24,
                        ] ).node().id = json.id;
                        table.draw(false);
                        _hesapKodu.val('');
                        _unvan.val('');
                        _ad.val('');
                        _soyad.val('');
                        _aktifPasif.val(0);
                        _field1.val(0);
                        _field2.val(0);
                        _field3.val('');
                        _field4.val('');
                        _field5.val('');
                        _field6.val('');
                        _field7.val('');
                        _field8.val('');
                        _resim.val('default.jpg');
                        _field10.val('');
                        _field11.val('');
                        _field12.val('');
                        _field13.val(0);
                        _field14.val(0);
                        _field15.val('');
                        _field16.val('');
                        _field17.val('');
                        _field18.val('');
                        _field19.val('');
                        _field20.val('');
                        _field21.val('');
                        _field22.val('');
                        _field23.val('');
                        _field24.val('');
                        modal.style.display = "none";
                        console.log("mrb")
                    }
                },
    
                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        }
        /*    FOR SUBMIT    */

    //--->Seçilen satırların silinmesi için listeye ekleme ve çıkarma işlemi

    function delete_list_element(url, data_delete_ids) {
        if (confirm('Are you sure you want to delete this survey?')) {
            console.log(data_delete_ids)
            $.ajax({
                url: url, // the endpoint
                type: "POST", // http method
                data: {
                    "data_delete_ids": data_delete_ids,
                }, // data sent with the post request

                // handle a successful response
                success: function (json) {
                    console.log(json); // log the returned json to the console
                    console.log("success"); // another sanity check

                    if (json.error) {
                        alert(json.result);
                    } else {
                        console.log(json)
                        table.row('.selected').remove().draw( false );
                        
                    }
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        }
        return false;
    }

    /*    FOR DATATABLE    */
});