const $ = window.$;

$('document').ready(function () {
  function fetchTranslation () {
    const langCode = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?';

    $.get(url + $.param({ lang: langCode }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  }

  $('INPUT#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Check if "Enter" key is pressed
      fetchTranslation();
    }
  });
});
