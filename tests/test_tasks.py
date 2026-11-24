import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes

class TestTasks(unittest.TestCase):
    def test_agregar_tarea_con_categoria_valida(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_con_categoria_vacia(self):
        with self.assertRaises(ValueError):
            agregar_tarea([], "Leer documentación", "   ")

    def test_pendientes_filtradas_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Enviar reporte", "Trabajo")
        self.assertEqual(
            pendientes(tareas, "ESTUDIO"),
            [tareas[0]],
        )

    def test_pendientes_categoria_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(pendientes(tareas, "Personal"), [])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_eliminar_tarea_existente(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Practicar")
        eliminada = eliminar_tarea(tareas, 1)
        self.assertIs(eliminada, tarea)
        self.assertEqual(tareas, [])

    def test_eliminar_tarea_id_inexistente(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Practicar")
        with self.assertRaisesRegex(ValueError, "^Tarea no encontrada$"):
            eliminar_tarea(tareas, 99)
        self.assertEqual(tareas, [tarea])

    def test_eliminar_tarea_conserva_las_demas(self):
        tareas = []
        agregar_tarea(tareas, "Primera")
        agregar_tarea(tareas, "Segunda")
        tercera = agregar_tarea(tareas, "Tercera")
        eliminar_tarea(tareas, 2)
        self.assertEqual([tarea["id"] for tarea in tareas], [1, 3])
        self.assertIn(tercera, tareas)

if __name__ == "__main__":
    unittest.main()
