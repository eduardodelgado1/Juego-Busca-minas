<div align="center">
  <h1>🚀 PyMinesweeper: Engine de Lógica Matemática y Computación Gráfica</h1>
  <p><i>Un desarrollo modular basado en Python y Pygame enfocado en la eficiencia algorítmica y la separación de responsabilidades.</i></p>

  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Pygame-Multimedia-green?style=for-the-badge" alt="Pygame">
  <img src="https://img.shields.io/badge/Architecture-Modular-orange?style=for-the-badge" alt="Modular Architecture">
</div>

<hr>

<h2>📋 Descripción del Proyecto</h2>
<p>
  Este proyecto no es solo una recreación del clásico "Busca Minas", sino una implementación técnica que demuestra el uso de <b>Programación Orientada a Objetos (POO)</b> avanzada y optimización de procesos en tiempo real. El sistema permite la configuración dinámica de la complejidad del entorno de juego mediante una interfaz paramétrica, gestionando una matriz de datos reactiva.
</p>

<h2>🛠️ Pilares Técnicos y Procesos Implementados</h2>

<h3>1. Arquitectura de Separación de Responsabilidades (SoC)</h3>
<p>
  El software ha sido diseñado bajo el principio de <b>Single Responsibility Principle (SRP)</b>. La lógica se segmenta en módulos independientes para facilitar la escalabilidad y el mantenimiento:
</p>
<ul>
  <li><b>Gestión de Estado (<code>tablero.py</code>, <code>pieza.py</code>):</b> Control absoluto del modelo de datos, independiente de la representación visual.</li>
  <li><b>Controlador de Interfaz (<code>ajustes.py</code>):</b> Implementación de widgets personalizados (sliders y botones) mediante el manejo de primitivas gráficas.</li>
  <li><b>Motor de Ejecución (<code>juego.py</code>):</b> Orquestador que coordina la comunicación entre el modelo de datos y el sistema de renderizado.</li>
  <li><b>Gestor de Recursos (<code>gestor_recursos.py</code>):</b> Sistema de caché para la carga optimizada de assets, reduciendo el overhead de I/O en disco.</li>
</ul>

<h3>2. Algoritmia de Propagación: Breadth-First Search (BFS)</h3>
<p>
  Para el revelado de casillas vacías, se implementó un algoritmo de <b>Búsqueda en Anchura (BFS)</b> utilizando una estructura de <code>collections.deque</code>. 
</p>
<div style="background-color: #f6f8fa; padding: 15px; border-radius: 6px; border: 1px solid #d0d7de; font-family: monospace;">
  // Lógica técnica de revelado<br>
  - Evita la recursión profunda para prevenir el desbordamiento de pila (Stack Overflow) en tableros de gran escala.<br>
  - Complejidad temporal O(V + E), garantizando una respuesta instantánea al usuario.
</div>

<h3>3. Patrón Flyweight para Gestión de Memoria</h3>
<p>
  El <code>GestorRecursos</code> implementa una variante del patrón Flyweight al pre-cargar y escalar las imágenes en un diccionario de caché. Esto asegura que, independientemente del tamaño del tablero (ej. 20x20), el sistema solo mantenga una instancia única de cada textura en memoria RAM, optimizando el rendimiento gráfico.
</p>

<h2>🚀 Instalación y Despliegue</h2>

<p>Asegúrate de tener un entorno de Python 3.x y la librería Pygame instalada:</p>
