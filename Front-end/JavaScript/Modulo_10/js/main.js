$(document).ready(function () {
    $('#carousel-imagens').slick({
        autoplay: true
    });

    $('.menu-hamburguer').click(function () {
        $('nav').slideToggle();
    })

    $('#tel').mask('(00) 00000-0000')

    $('form').validate({
        rules: {
            nome: {
                required: true
            },
            email: {
                required: true,
                email: true
            },
            tel: {
                required: true
            },
            msg: {
                required: true
            },
            veiculoInteresse: {
                required: false
            }
        },
        messages: {
            nome: 'Por favor, insira seu nome'
        },
        submitHandker: function (form) {
            console.log(form)
        },
        invalidHandler: function (evento, validador) {
            let camposIncorretos = validador.numberOfInvalids();
            console.log(camposIncorretos)
        }
    })

    $('.lista-veiculos button').click(function(){
        const destino = $('#contato');
        const nomeVeiculo= $(this).parent().find('h3').text();

        $('#veiculo-interesse').val(nomeVeiculo);

        $('html').animate({
            scrollTop: destino.offset().top
        }, 1000)
    })
})