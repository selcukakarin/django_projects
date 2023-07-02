$(document).ready(function () {
    let _hesapKodu = $('#hesapKodu')
    let _unvan = $('#unvan')
    let _ad = $('#ad')
    let _soyad = $('#soyad')
    let _aktifPasif = $('#aktifPasif')
    
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
                        console.log(json.id)
                        // table.row.add( [
                        //     json.id,
                        //     json.hesapKodu,
                        //     json.unvan,
                        //     json.ad,
                        //     json.soyad,
                        //     json.aktifPasif,
                            
                        // ] ).node().id = json.id;
                        table.row
                        .add({"id":json.id,
                            "hesapKodu":json.hesapKodu,
                            "unvan":json.unvan,
                            "ad":json.ad,
                            "soyad":json.soyad,
                            "aktifPasif":json.aktifPasif,})
                        .draw();
                        table.draw(false);
                        _hesapKodu.val('');
                        _unvan.val('');
                        _ad.val('');
                        _soyad.val('');
                        _aktifPasif.val(0);
                        
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