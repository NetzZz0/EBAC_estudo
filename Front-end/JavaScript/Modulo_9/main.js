$(document).ready(function () {
    $('header button').click(function () {
        $('form').slideDown();
    })

    $('#reset-button').click(function () {
        $('form').slideUp();
    })

    $('form').on('submit', function (e) {
        e.preventDefault();
        const adressNewImg = $('#adress-new-img').val();
        const newItem = $('<li style="display: none;"></li>');
        $(`<img src="${adressNewImg}" />`).appendTo(newItem);
        $(`
            <div class="img-link">
                <a href="${adressNewImg}" target="_black" title="Ver em tamanho real">Ver imagem em tamanho real</a>
            </div>
            `).appendTo(newItem);
        $(newItem).appendTo('ul');
        $(newItem).fadeIn(1000);
        $('#adress-new-img').val('')
    })
}) 