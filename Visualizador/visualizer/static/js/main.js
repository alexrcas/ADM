$('.timeSeries').hide();

$('#btn-load').on('click', () => {
    let val = $('#input-url').val()
    fetch(`/data`, {
        method: 'POST',
        body: JSON.stringify({'url': val}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(res => {
        res.headers.forEach(key => {
            $('#select-x')
            .append($('<option></option>') 
            .attr('value', key)
            .text(key))

            $('#select-y')
            .append($('<option></option>')
            .attr('value', key)
            .text(key))

            $('#btn-send').attr('disabled', false)
        })

        console.log(res.timeSeries)
        if (res.timeSeries == true) {
            $('.x-panel').hide()
            $('.y-panel').show()
            $('.timeSeries').show();
        }
        else {
            $('.x-panel').show()
            $('.y-panel').show()
            $('.timeSeries').hide();

        }
    })
})

$('#btn-hist').on('click', () => {
    data = {'url': $('#input-url').val(), 'y': $('#select-y').val()}
    $.ajax({
        url: '/distribution',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: res => {document.write(res)}
    })
})