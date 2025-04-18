<?php
$cvUrl = $_GET['cvUrl'] ?? '';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>CV Viewer</title>
    <link rel="stylesheet" href="https://mozilla.github.io/pdf.js/web/viewer.css">
    <style>
        html,
        body {
            margin: 0;
            height: 100%;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
    <!-- PDF.js Viewer -->
    <link rel="stylesheet" href="https://mozilla.github.io/pdf.js/web/viewer.css">
    <script src="https://mozilla.github.io/pdf.js/build/pdf.js"></script>
    <script src="https://mozilla.github.io/pdf.js/web/viewer.js"></script>

</head>

<body>
    <iframe src="/pdfjs/web/viewer.html?file=<?= urlencode($cvUrl) ?>"></iframe>
</body>

</html>