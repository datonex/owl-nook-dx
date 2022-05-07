var script = document.createElement('script');
script.type = 'text/javascript';
script.src =
  'https://cdn.tiny.cloud/1/oee2h6odxrg7bm4cofq0ahnk8g92ff8mlhxaopxxmkam5syc/tinymce/6/tinymce.min.js';
script.referrerPolicy = 'origin';
document.head.appendChild(script);
script.onload = function () {
  tinymce.init({
    selector: 'textarea',
    plugins: 'advlist autolink lists link image charmap preview anchor pagebreak visualblocks code',
    menubar: 'edit view insert format tools table help',
    toolbar:
      'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | ' +
      'bullist numlist outdent indent | link image | media fullscreen | ' +
      'emoticons | help',
    toolbar_mode: 'floating',
    content_style:
      "@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');",
  });
};
