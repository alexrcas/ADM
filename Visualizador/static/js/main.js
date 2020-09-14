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
            $('.y-panel').hide()
        }
        else {
            $('.x-panel').show()
            $('.y-panel').show()
        }
    })
})