from django.test import TestCase


class InicioViewTest(TestCase):
    def test_inicio_responde_correctamente(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "URL y Vistas")
