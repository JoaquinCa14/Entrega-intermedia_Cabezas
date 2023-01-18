# Entrega-intermedia_Cabezas

Mi nombre es Joaquin Cabezas y soy estudiante de informatica!
Este es mi intermedio con miras al proyecto final.

Cree una página simulando la empresa "Agroinsumos JOCAM", página que aun no esta completa ya que esta cumple con los requisitos de la entrega de intermedio.

Para empezar, mi pagina cuenta con un INDEX donde se encuentra el nombre de la pagina, sus 4 botones correspondientes con sus 3 clases y un boton de Inicio.

En el boton listado de productos encontramos la opcion para crear un nuevo producto, nos lleva al template de crear productos, pudiendo asi ingresar el mismo, con los atributos "nombre", "precio" y la opcion stock en todo caso que querramos mostrar que si o que no hay.

A su lado encontramos el 2do boton "Listado de ordenes" donde nos guardara los datos del consultante, la hora y su metodo de pago.
Y por ultimo encontramos el boton "Listado de proveedores, el cual nos lleva a un template aparte donde poder registrar el proveedor. Esta contiene los atributos "nombre", "direccion", "numero de telefono" y "email". Tambien tenemos un boton que nos permite crear el proveedor una vez ingresado el mismo.

En la misma navbar tambien tenemos un Search, que funciona como filtro de los productos ingresados. Ingresando el nombre de uno de los productos, nos filtra la busqueda y nos muestra unicamente el producto que lleva ese nombre.

Trabaje en herencia de html con la etiqueta {% extends 'base.html'%} en los templates "providers", "products" y "orders" que heredan el patrón de diseño del template "base".

Todavia quedan detalles de imagenes de productos y otras cosas del diseño de la pagina que me gustaria agregar y modificar, pero este intermedio tiene todos los requisitos pedidos.
