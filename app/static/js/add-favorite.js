$(document).on('submit', '#save_favorite', function (e) {
    e.preventDefault()
    form = $(this);
    $.ajax({
        type: 'POST',
        url: e.currentTarget.getAttribute('action'),
        data: {
            product: e.currentTarget[1].value,
            substitute: e.currentTarget[2].value,
            csrfmiddlewaretoken: e.currentTarget[0].value,
            action: 'post'
        },
        success: function (json) {
            form.after("<div><button class='btn btn-success active save_button btn-block' disabled><i class='fas fa-check'></i> Sauvegardé</button></div>");
            form.remove();
            alert('Le produit a bien été enregistré en favori')
        },
        error: function (json) {
            alert('Une erreur est survenue lors de la sauvegarde');
        }
    });
});