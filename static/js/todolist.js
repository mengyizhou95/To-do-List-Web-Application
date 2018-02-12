$(document).ready(function () {
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  $('.new-todo').keydown(function (event) {
    if (event.which === 13) {
      if (!event.target.value.trim()) {
        return;
      }


      $.post('/add/', {
        'action': 'add',
        'content': event.currentTarget.value
      }, function () {
        window.location.href = '/';
      })
    }
  });

  $('.toggle').click(function (e) {
    var hidden = $(this).parent().children()[0];
    $.get('/complete/' + hidden.id, function () {
      window.location.href = '/';
    })
  });

  $('.destroy').click(function (e) {
    var hidden = $(this).parent().children()[0];
    $.get('/delete/' + hidden.id, function () {
      window.location.href = '/';
    })
  });

  $('.show_all').click(function (e) {
    window.location.href = '/';
  });

  $('.show_active').click(function (e) {
    window.location.href = '/active';
  });

  $('.show_completed').click(function (e) {
    window.location.href = '/completed';
  })

});