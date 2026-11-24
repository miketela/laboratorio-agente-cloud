def agregar_tarea(tareas, titulo, categoria="General"):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    if categoria is None:
        raise ValueError("La categoría es obligatoria")
    categoria = categoria.strip()
    if not categoria:
        raise ValueError("La categoría es obligatoria")
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "categoria": categoria,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea

def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")

def pendientes(tareas, categoria=None):
    pendientes = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return pendientes
    categoria = categoria.strip()
    if not categoria:
        return pendientes
    categoria = categoria.casefold()
    return [
        t for t in pendientes
        if t.get("categoria", "").casefold() == categoria
    ]
