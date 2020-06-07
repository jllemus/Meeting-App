$(document).ready(() => {
    $('.get-meetings').click(() => {
        $.ajax({
            url: '/validate_meeting',
            type: 'GET',
            success: (data) => {
                console.log('Success');
                document.getElementById("meetings").innerHTML = data;
            }
        })
    })


})

function myFunction(id){
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(token)
    $.ajax({
        url: '/delete_item/delete/' + id ,
        type: 'GET',
        success: () => {
            alert("Item " + id + " deleted")
        },
        error: (data)=>{
            console.log(data)
        }
    })
}

$(function () {
    $("#date-time-meeting").datetimepicker({
        format: 'YYYY-MM-DD',
    });
});