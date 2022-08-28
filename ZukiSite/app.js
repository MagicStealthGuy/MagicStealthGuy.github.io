import { toPng } from 'html-to-image';

var node = document.getElementById('zuki-card-node');

toPng(node)
  .then((dataUrl) => {
    const img = new Image();
    img.src = dataUrl;
    document.body.appendChild(img);
  })
  .catch(function (error) {
    console.error('oops, something went wrong!', error);
  });