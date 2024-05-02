const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware para parsear el cuerpo de las peticiones JSON
app.use(bodyParser.json());

app.post('/webhook', (req, res) => {
    console.log('Webhook recibido:');
    console.log(req.body); // Aquí puedes ver el cuerpo del webhook recibido

    // Aquí puedes agregar lógica para manejar el webhook, por ejemplo, verificar el tipo de evento y actuar en consecuencia

    res.status(200).send('Webhook recibido');
});

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
